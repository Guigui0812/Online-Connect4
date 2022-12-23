import socket

host, port = 'localhost', 12345
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    
    socket.connect((host, port))
    print("client is connected to server")

    data = "Hello, world!"
    data = data.encode("utf8")

    socket.sendall(data)
    print("client sent data to server")

    data = socket.recv(1024)
    print("client received", data)

    socket.close()
    print("client closed connection")

except ConnectionRefusedError:

    print("client failed to connect to server")

finally:

    socket.close()
    print("client closed connection")

