import socket
import threading
import time

class Connection:

    # Initialize the connection class
    def __init__(self, host, port):
        # Create the socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host, self.port = host, int(port)
        self.server_alive = False

        # keep alive thread to keep the connection alive
        self.keep_alive_thread_running = True
        self.keep_alive_thread = threading.Thread(target=self.keep_alive_message)
        self.keep_alive_thread.start()

    # Method to connect to the server
    def connect(self):
        try:
            self.socket.connect((self.host, self.port))
            print("client is connected to server")
            return True
        except:
            print("client failed to connect to server")
            return False

    def server_alive(self):
        
        if self.server_alive == True:
            return True
        else:
            return False

    # Check if the server is still alive
    def keep_alive_message(self):

        # while the thread is running send a keep alive message to the server
        while self.keep_alive_thread_running:
            self.send_string("keep_alive")
            data = self.receive_string()

            if data == "keep_alive":
                self.server_alive = True
                time.sleep(1)
            else:
                print("server is not alive")
                self.server_alive = False
                self.close()
                self.keep_alive_thread_running = False
        
    # Send a string to the server
    def send_string(self, data):
        try:
            data = data.encode("utf8")
            self.socket.sendall(data)
            print("client sent ", data)
        except ConnectionRefusedError:
            print("client failed to send data to server")

    # Receive a string from the server
    def receive_string(self):
        try:
            data = self.socket.recv(1024)
            data = data.decode("utf8")
            print("client received ", data)
            return data
        except ConnectionAbortedError:
            print("client failed to receive data from server")

    # Send data to the server
    def send_data(self, data):
        try:
            self.socket.sendall(data)
            print("client sent ", data)
        except ConnectionRefusedError:
            print("client failed to send data to server")

    # Receive data from the server
    def receive_data(self):
        try:
            data = self.socket.recv(1024)
            print("client received ", data)
            return data
        except ConnectionRefusedError:
            print("client failed to receive data from server")

    # Close the connection
    def close(self):
        try:
            self.socket.close()
            print("client closed connection")
        except ConnectionRefusedError:
            print("client failed to close connection")
