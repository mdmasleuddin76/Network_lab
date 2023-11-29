import socket

# Define the host and port to listen on
HOST = '127.0.0.1'
PORT = 12345

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# Accept a connection from a client
client_socket, client_address = server_socket.accept()
print(f"Accepted connection from {client_address}")

# Receive and print messages from the client
while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
        break
    print(f"Received from client: {data}")

    # Send a response back to the client
    response = f"Server received: {data}"
    msg=input("Enter message to send (type 'exit' to quit): ")
    client_socket.send(msg.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()
