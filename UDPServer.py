import socket

# Define the host and port to bind to
HOST = '127.0.0.1'
PORT = 12345

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

print(f"UDP Server is listening on {HOST}:{PORT}")

while True:
    # Receive data and address from the client
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from {client_address}: {data.decode('utf-8')}")

    # Send a response back to the client
    response = f"Server received: {data.decode('utf-8')}"
    msg=input("Enter message to send (type 'exit' to quit): ")
    server_socket.sendto(msg.encode('utf-8'), client_address)
