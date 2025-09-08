import socket

class Server:
    def __init__(self) -> None:
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(("127.0.0.1", 5000))
        self.server.listen(1)
        self.socketServer()

    def socketServer(self):
        connection, address = self.server.accept()

        data = connection.recv(1024).decode("UTF-8")

        print("Message from Client received: ", data)

        connection.sendall("Your message was received succesfully".encode("UTF-8"))

        connection.close()
        self.server.close()