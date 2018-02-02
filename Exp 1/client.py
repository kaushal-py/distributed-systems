import socket

class ChatClient:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    def configure(self, host, port):
        self.socket.connect((host, port))

    def connect(self):


        while True:
            client_message = input("Type a message to send : ")

            if client_message == "Stop":
                break
            self.socket.send(client_message.encode('UTF-8'))

            print("Waiting for message from server..")
            server_message = self.socket.recv(1024).decode('UTF-8')
            print("Server said ", server_message)
        self.socket.close()

if __name__ == "__main__":
    client = ChatClient()
    client.configure(socket.gethostname(), 8080)
    client.connect()
