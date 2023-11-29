import socket

# Define the server address and port
SERVER_HOST = '127.0.0.1'
SERVER_PORT = 12345

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Get user input and send it to the server
    message = input("Enter message to send (type 'exit' to quit): ")
    if message.lower() == 'exit':
        break

    client_socket.sendto(message.encode('utf-8'), (SERVER_HOST, SERVER_PORT))

    # Receive and print the response from the server
    response, _ = client_socket.recvfrom(1024)
    print(f"Server response: {response.decode('utf-8')}")

# Close the socket
client_socket.close()
