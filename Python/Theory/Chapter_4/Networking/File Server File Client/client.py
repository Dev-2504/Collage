import socket

# Server configuration
HOST = 'localhost'  # Server address (same as server)
PORT = 5001         # Port number (same as server)

# Create socket
client_socket = socket.socket()
client_socket.connect((HOST, PORT))

# Receive file data
data = b''
while True:
    packet = client_socket.recv(1024)
    if not packet:
        break
    data += packet

# Save the file
with open('received.txt', 'wb') as file:
    file.write(data)

print("File received successfully.")

# Close connection
client_socket.close()
