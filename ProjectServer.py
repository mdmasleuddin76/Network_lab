import random
import socket
import threading
import json

print("\033c")

PORT = 4000
# size of data in bytes that can go in one packets
HEADER = 1024
FORMAT = "utf-8"
MAX_CLIENT = 2
DISCONNECT_MESSAGE = "!DISCONNECTED!"
FIRST_CONNECTION = "!FIRST_CONNECTION!"
SERVER = '192.168.43.61'
ADDRESS = (SERVER, PORT)
MAX_SIZE = 1000001

# stores the client information like username
user_list = {}
list_of_keys = {}

#######################################################################
def decrypt_message(s, key):
    ans = ""
    mat = [[' ' for _ in range(key)] for _ in range((len(s) - 1) // key + 1)]
    k = 0
    n=int((len(s) - 1) // key + 1)
    for i in range(key):
        for j in range(n):
            if k < len(s):
                mat[j][i] = s[k]
                k += 1

    for i in range(n):
        for j in range(key):
            ans += mat[i][j]

    return ans
#######################################################################

"""
Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_STREAM. AF_INET refers to the address-family ipv4. The SOCK_STREAM means connection-oriented TCP protocol.  
"""
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f"[UNABLE TO CREATE SOCKET] : {err}...\n")
    exit(0)

"""
A server has a bind() method which binds it to a specific IP and port so that it can listen to incoming requests on that IP and port.  
"""
try:
    server.bind(ADDRESS)
except socket.error as err:
    print(f"[UNABLE TO BIND TO THE SPECIFIC IP AND PORT] : {err}...\n")
    exit(0)


def somemessagedeleter(msg):
    offensive_words = ["dummy1", "dummy2", "dummy3", "dummy4", "dummy5", "dummy6", "dummy7", "dummy8", "dummy9"]
    replace_words ={
        "jamia":" jamia millia islamia ",
        "delhi":" New Delhi ",
        "Engg":" Engineering ",
    }
    for word in offensive_words:
        if word in msg:
            first=msg.find(word)
            if first==0:
                msg=msg.replace(f"{word} ", "")
            elif first==len(msg)-len(word):
                msg=msg.replace(f" {word}", "")
            else:
              msg = msg.replace(f" {word} ", " ")
    for key,value in replace_words.items():
        if key in msg:
            msg = msg.replace(f" {key} ",value)
            # msg=msg.replace(f" {key}",value)
            # msg=msg.replace(f"{key} ",value)
    return msg
# send message to the client


def sendMessage(msg, client_connection, client_address):
    try:
        global user_list
        global list_of_keys
        client_object = json.loads(msg)
        name=client_object['Reciever']
        if name.lower() != "all":
          clco = list_of_keys.get(name, {}).get('client_connection', None)
          if clco:
             clco.send(msg.encode(FORMAT))
          else:
           temp={"name":"Server","decrypted":f"Unable to send message to {name}"}
           errmessage=json.dumps(temp)
           client_connection.send(errmessage.encode(FORMAT))
        else:
            for key,data in list_of_keys.items():
               cl_conn=data.get('client_connection',None)
               if cl_conn:
                cl_conn.send(msg.encode(FORMAT))
                
    except socket.error as err:
        #global user_list
        print(
            f"[UNABLE TO SEND MESSAGE TO THE {user_list[client_address]['name']}] : {err}...\n")
        del user_list[client_address]
        # exit the helper thread created not the main thread
        exit(0)

# decode the message if it was the first message or the other message and respond accordingly


def decodeMessage(str, client_connection, client_address):
    client_object = json.loads(str)
    if client_object['msg'] == FIRST_CONNECTION:
        global user_list
        global list_of_keys
        user_list[client_address] = {
            "name":  client_object['name'],
        }
        list_of_keys[client_object['name']] = {
            "client_address": client_address,
            "client_connection": client_connection,
        }
        return f"joined the server."
    else:
        msg = client_object["msg"]
        dcrptd_msg = client_object["decrypted"]
        print(msg)
        sendMessage(str, client_connection, client_address)
        return dcrptd_msg

# handle's client queries


def handleClient(client_connection, client_address):
    print(f"[NEW CONNECTION] {client_address} connected.\n")
    global user_list
    connected = True
    while connected:
        # reciveing response from client
        try:
            str = client_connection.recv(HEADER).decode(FORMAT)
        except socket.error as err:
            print(
                f"[UNABLE TO RECIVE MESSAGE FROM THE {user_list[client_address]['name']}] : {err}...\n")
            del user_list[client_address]
            # exit the helper thread created not the main thread
            exit(0)

        if len(str) == 0:
            continue

        msg = decodeMessage(str, client_connection, client_address)
        if msg == DISCONNECT_MESSAGE:
            # disconnect the client from the server if message is !DISCONNECTED!
            connected = False
            print(f"{user_list[client_address]['name']} is offline now.")
            continue
        if client_address in user_list and 'key' in user_list[client_address]:
         msg = decrypt_message(msg, int(user_list[client_address]['key']))
        print(f"{user_list[client_address]['name']} : {msg}")

    # removing the client from the list after he/she get disconnected
    del user_list[client_address]
    client_connection.close()


def start():
    """
    A server has a listen() method which puts the server into listening mode. This allows the server to listen to incoming connections.
    """
    server.listen(MAX_CLIENT)
    print(f"[LISTENING]  server is listening on {SERVER}\n")
    connected = True
    while connected:
        """
        And last a server has an accept() and close() method. The accept method initiates a connection with the client and the close method closes the connection with the client. 
        """
        try:
            client_connection, client_address = server.accept()
        except socket.error as err:
            print(f"[UNABLE TO CONNECT TO THE CLIENTS] : {err}...\n")
            exit(0)

        try:
            thread = threading.Thread(target=handleClient, args=(
                client_connection, client_address))
            thread.start()
        except socket.error as err:
            print(f"[UNABLE TO CREATE THREAD] : {err}...\n")
            exit(0)

        # -1 bcoz one thread is running the server
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}\n")


print("[STARTING] server is starting...\n")
start()