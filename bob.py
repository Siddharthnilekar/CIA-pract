import socket
import threading
import time

class BobServer:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 12345
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        self.connections = []

    def handle_client(self, conn, addr):
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024).decode()
            print("Received:", data)
            if data.lower() == "yes":
                response = "Hello Alice! Welcome to the server."
                conn.send(response.encode())
            else:
                response = "Goodbye Alice."
                conn.send(response.encode())

    def start(self):
        print("Server listening on", (self.host, self.port))
        while True:
            conn, addr = self.server_socket.accept()
            self.connections.append(conn)
            threading.Thread(target=self.handle_client, args=(conn, addr)).start()

def main():
    bob_server = BobServer()
    bob_server.start()

if __name__ == '__main__':
    main()
