import socket, threading, datetime, time

class Client(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.host = "127.0.0.1"
        self.port = int(input("contact:"))
        self.username = input("username:")

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:
            try:
                s.connect((self.host, self.port))
            except:
                print("connection failed, trying again in 5 seconds")
                time.sleep(5)
                continue
            break

        message = ""

        while message != "Quit":
            message = input("msg:")
            try:
                s.sendall((self.username + ": " + message).encode())
            except:
                print("message could not be sent")
                break
        s.close()

class Server(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.host = "127.0.0.1"
        self.port = 5010

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.host, self.port))
        except:
            print("socket could not be bound to the address")
            s.close()

        s.listen(1)

        try:
            conn, addr = s.accept()
        except:
            print("connection failed")

        quitting = False

        while not quitting:
            data = conn.recv(1024).decode()
            if "Quit" in data:
                quitting = True
            elif data != "":
                print("received from " + data + " (" + datetime.datetime.now().strftime('%H:%M') + ")")
        s.close()

def main():
    server = Server()
    server.start()

    client = Client()
    client.start()


if __name__ == "__main__":
    main()

