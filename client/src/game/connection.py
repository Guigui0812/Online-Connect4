import socket
import threading
import time
import json

# Represents a connection to the server
class Connection:

    # Initialize the connection class
    def __init__(self, host, port):

        # Create the socket
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host, self.port = host, int(port)
        self.server_alive = True 

        # keep alive thread to handle connection break
        self.lock = threading.Lock()
        self.keep_alive_thread_running = True
        self.keep_alive_thread = threading.Thread(target=self.send_keep_alive)

    # Method to connect to the server
    def connect(self):
        try:
            self.socket.connect((self.host, self.port)) # connect to the server
            print("client is connected to server") # print a message to the console
            self.keep_alive_thread.start() # start the keep alive thread
            return True
        except:
            print("client failed to connect to server")
            return False

    # Check if the server is still alive
    def check_alive(self):

        print(self.server_alive)

        if self.server_alive == True:    
            return True
        else:
            return False
           
    # Check if the server is still alive
    def send_keep_alive(self):

        # while the thread is running send a keep alive message to the server
        while self.keep_alive_thread_running == True:       

            # send a keep alive message to the server as a json
            data_to_send =  {"message_type": "keep_alive"}
            data_to_send = json.dumps(data_to_send)
            self.send_string(data_to_send)

            response = self.receive_string()

            # if the server is not alive or if the other player left, we stop the thread
            if response == "player_lost": 

                self.server_alive = False
                self.keep_alive_thread_running = False
         
            time.sleep(10)
        
    # Send a string to the server
    def send_string(self, data):
        try:
            print(data)
            data = data.encode("utf8")

            with self.lock:
                self.socket.sendall(data)
            
        except ConnectionRefusedError:
            print("client failed to send data to server")

    # Receive a string from the server
    def receive_string(self):
        try:
            with self.lock:
                data = self.socket.recv(1024)

            if data != b'':
                print(data)
                data = data.decode("utf8")
                return data
        except ConnectionAbortedError:
            print("client failed to receive data from server")

    # Send data to the server
    def send_data(self, data):
        try:
            print(data)
            with self.lock:
                self.socket.sendall(data)
                
        except ConnectionRefusedError:
            print("client failed to send data to server")

    # Receive data from the server
    def receive_data(self):
        try:
            with self.lock:
                data = self.socket.recv(1024)              
            if data != b'':         
                return data
        except ConnectionRefusedError:
            print("client failed to receive data from server")

    # Close the connection
    def close(self):
        try:
            self.keep_alive_thread_running = False  
            with self.lock:
                self.socket.close()
            print("connection closed")
        except ConnectionRefusedError:
            print("client failed to close connection")