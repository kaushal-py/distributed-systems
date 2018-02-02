import socket

class ChatServer:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Server Initialised.")

    def configure(self, host, port):
        self.socket.bind((host, port))
        # queue up to 5 requests
        self.socket.listen(5) 
        print("Server starting at ", host, ":", port)

    def run(self):
        print("Server running...")

        # establish a connection
        clientsocket,addr = self.socket.accept()      

        while True:
            print("Waiting for message from client..")
            client_message = clientsocket.recv(1024).decode('UTF-8')

            print(addr, "said :", client_message)

            server_mesage = input("Type a message to send : ")
            clientsocket.send(server_mesage.encode('UTF-8'))
        clientsocket.close()

if __name__ == "__main__":
    server = ChatServer()
    server.configure(socket.gethostname(), 8080)
    server.run()