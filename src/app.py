from time import sleep
from client import Client
from server import Server
import threading
from os import system

class App:
    def __init__(self) -> None:
        self.menu()

    def menu(self):
        while True:
            try:
                print("Socket API 🖥️ 🛜")
                print()

                options = [

                    "1- Send Message to the Server",
                    "2- Exit"
                ]

                for option in options:
                    print(option)
                    sleep(0.5)
                print()

                userInput = int(input("Choose an option: "))
                print()
                system("cls")

                if userInput not in [1, 2]:
                    print("Error! Choose a valid option!")
                    continue
                
                elif userInput == 1:
                    serverThread = threading.Thread(target=Server)
                    serverThread.start()

                    sleep(1)

                    client = Client()
                    clientInput = input("Send a message to the server: ")
                    print()
                    client.socketClient(clientInput)

                    input("Click Enter to exit!")
                    system("cls")

                elif userInput == 2:
                    break

                else:
                    print("Error! Choose a valid option")
                    print()

            except ValueError:
                print("Error! Choose a valid option")
                print()
                continue