import socket

def main():
    host = '127.0.0.1'
    port = 12345

    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((host, port))

    print(f"Server listening on {host}:{port}")

    while True:
        data, addr = server.recvfrom(1024)
        print(f"Received request from {addr[0]}:{addr[1]}")
        response = "Server response: Request received and processed."
        server.sendto(response.encode('utf-8'), addr)

if __name__ == "__main__":
    main()
