import socket

# Server configuration
HOST = 'localhost'   # Server address
PORT = 5001          # Port number

# Create socket
server_socket = socket.socket()
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server listening on {HOST}:{PORT}...")

conn, addr = server_socket.accept()
print(f"Connection from {addr}")

# File to send
filename = 'sample.txt'  # This file should be in the same folder
with open(filename, 'rb') as file:
    data = file.read()

# Send file data
conn.sendall(data)
print("File sent successfully.")

# Close connection
conn.close()
server_socket.close()
