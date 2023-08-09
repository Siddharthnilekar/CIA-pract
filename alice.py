import socket

def main():
    host = '127.0.0.1'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        message_to_send = input("Do you want to connect to Bob's server? (yes/no): ")
        client_socket.send(message_to_send.encode())
        response = client_socket.recv(1024).decode()
        print("Received response:", response)

if __name__ == '__main__':
    main()
