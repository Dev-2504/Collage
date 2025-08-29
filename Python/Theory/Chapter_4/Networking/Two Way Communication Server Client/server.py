import socket

HOST = 'localhost'
PORT = 5002

# Create socket
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}...")
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive message from client
    client_msg = conn.recv(1024).decode()
    if client_msg.lower() == 'exit':
        print("Client ended the chat.")
        break
    print(f"Client: {client_msg}")

    # Send reply to client
    server_msg = input("Server: ")
    conn.send(server_msg.encode())
    if server_msg.lower() == 'exit':
        print("Server ended the chat.")
        break

conn.close()
server_socket.close()
