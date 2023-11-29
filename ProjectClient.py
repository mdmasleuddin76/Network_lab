import socket
import json
import threading
import time

print("\033c")

PORT = 4000
HEADER = 1024
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECTED!"

SERVER = "192.168.43.61"
ADDRESS = (SERVER, PORT)

def encrypt_message(s, key):
    ans = ""
    n=int((len(s) - 1) // key + 1)
    mat = [[' ' for _ in range(key)] for _ in range((len(s) - 1) // key + 1)]
    k = 0
    
    for i in range(n):
        for j in range(key):
            if k < len(s):
                mat[i][j] = s[k]
                k += 1

    for i in range(key):
        for j in range(n):
            ans += mat[j][i]

    return ans



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



try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print(f"[UNABLE TO CREATE SOCKET] : {err}...\n")
    exit(0)

try:
    client.connect(ADDRESS)
except socket.error as err:
    print(f"[UNABLE TO CONNECT TO THE SERVER] : {err}...\n")
    exit(0)



def sendMessage(msg, key,reciever,user_name):
    encrypted_msg = encrypt_message(msg, key)
    json_object = {'msg': encrypted_msg, "key": key, "decrypted": msg,"Reciever":reciever,"name":user_name}
    msg = json.dumps(json_object)
    try:
        client.send(msg.encode(FORMAT))
    except socket.error as err:
        print(f"[UNABLE TO SEND MESSAGE TO THE SERVER] : {err}...\n")
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


def receiveMessage():
    try:
        # timeout = 60
        # client.settimeout(timeout)
        server_msg = client.recv(HEADER).decode('utf8')
        obj = json.loads(server_msg)
        msg=obj['decrypted']
        sender=obj['name']
        msg=somemessagedeleter(msg)
        print(f"\n{sender}",": ",f"{msg}\n\n""Enter The Text: ")
        # message_sender()
        return server_msg
    # except socket.timeout:
    #     print("Timeout: No message received within the specified time.")
    #     return None
    except socket.error as err:
        print(f"[UNABLE TO RECEIVE MESSAGE FROM THE SERVER] : {err}...\n")
        exit(0)
    # finally:
    #     client.settimeout(None)

def message_sender():
    while True:
        text = input("Enter The Text: ")
        recv=input("Enter The Reciever Name: ")
        sendMessage(text, key,recv,user_name)
        time.sleep(2)

def message_receiver():
    while True:
        server_msg = receiveMessage()
        time.sleep(2)

user_name = input("Enter your name : ")
json_object = {'name': user_name, 'msg': '!FIRST_CONNECTION!'}
msg = json.dumps(json_object)
client.send(msg.encode(FORMAT))

connected = True
key = int(input("Enter The Key: "))

# Create threads for sender and receiver functions
sender_thread = threading.Thread(target=message_sender)
receiver_thread = threading.Thread(target=message_receiver)

# Start both threads
sender_thread.start()
receiver_thread.start()

# Wait for both threads to finish (this won't happen in this example)
sender_thread.join()
receiver_thread.join()

# Closing the connection from the server
print("Connection Closed!")
client.close()
