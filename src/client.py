import socket

class Client:
    def __init__(self) -> None:
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(("127.0.0.1", 5000))

    def socketClient(self, message):
        self.client.sendall(message.encode("UTF-8"))
        print()

        data = self.client.recv(1024).decode("UTF-8")
        print("Message from Server: ", data)
        print()

        self.client.close()