import socket


class Network:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host, self.port = "localhost", 12345

    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print("client is connected to server")
            return True
        except:
            print("client failed to connect to server")
            return False

    def send_string(self, data):
        try:
            data = data.encode("utf8")
            self.socket.sendall(data)
            print("client sent ", data)
        except ConnectionRefusedError:
            print("client failed to send data to server")

    def receive_string(self):
        try:
            data = self.socket.recv(1024)
            data = data.decode("utf8")
            print("client received ", data)
            return data
        except ConnectionAbortedError:
            print("client failed to receive data from server")

    def send_data(self, data):
        try:
            self.socket.sendall(data)
            print("client sent ", data)
        except ConnectionRefusedError:
            print("client failed to send data to server")

    def receive_data(self):
        try:
            data = self.socket.recv(1024)
            print("client received ", data)
            return data
        except ConnectionRefusedError:
            print("client failed to receive data from server")

    def close(self):
        try:
            self.socket.close()
            print("client closed connection")
        except ConnectionRefusedError:
            print("client failed to close connection")
