import socket

HOST = 'localhost'
PORT = 5002

# Create socket
client_socket = socket.socket()
client_socket.connect((HOST, PORT))

while True:
    # Send message to server
    client_msg = input("Client: ")
    client_socket.send(client_msg.encode())
    if client_msg.lower() == 'exit':
        print("Client ended the chat.")
        break

    # Receive reply from server
    server_msg = client_socket.recv(1024).decode()
    if server_msg.lower() == 'exit':
        print("Server ended the chat.")
        break
    print(f"Server: {server_msg}")

client_socket.close()
