import socket

def main():
    host = '127.0.0.1'
    port = 12345

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = "Client request: Send me data"
    client.sendto(message.encode('utf-8'), (host, port))

    response, addr = client.recvfrom(1024)
    print("Received response:", response.decode('utf-8'))

    client.close()

if __name__ == "__main__":
    main()
