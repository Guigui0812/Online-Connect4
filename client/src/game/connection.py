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
        if self.server_alive == True:    
            return True
           
    # Check if the server is still alive
    def send_keep_alive(self):

        # while the thread is running send a keep alive message to the server
        while self.keep_alive_thread_running == True:               
            self.send_string("keep_alive")
            response = self.receive_string()
            
            if response == "keep_alive":                 
                self.server_alive = True
                
            elif response == "player_lost":               
                self.server_alive = False
         
            time.sleep(10)
        
    # Send a string to the server
    def send_string(self, data):
        try:
            data = data.encode("utf8")
            self.lock.acquire() # acquire the lock
            self.socket.sendall(data)
            self.lock.release() # release the lock
        except ConnectionRefusedError:
            print("client failed to send data to server")

    # Receive a string from the server
    def receive_string(self):
        try:
            self.lock.acquire() # acquire the lock
            data = self.socket.recv(1024)

            if data != b'':
                self.lock.release() # release the lock
                data = data.decode("utf8")
                return data
        except ConnectionAbortedError:
            print("client failed to receive data from server")

    # Send data to the server
    def send_data(self, data):
        try:
            self.lock.acquire() # acquire the lock
            self.socket.sendall(data)
            self.lock.release() # release the lock
            #print("client sent ", data)
        except ConnectionRefusedError:
            print("client failed to send data to server")

    # Receive data from the server
    def receive_data(self):
        try:
            self.lock.acquire() # acquire the lock
            data = self.socket.recv(1024)
            if data != b'':
                self.lock.release() # release the lock
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
