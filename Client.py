import socket, threading, time, sys

class Client(threading.Thread):

    def __init__(self, ip, port, user, msg):
        threading.Thread.__init__(self)
        self.hostIP = ip
        self.port = port
        self.username = user
        self.message = msg

    def setHostIP(self, host):
        self.host = host

    def setPort(self, port):
        self.port = port

    def setUsername(self, username):
        self.username = username

    def run(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error:
            print("Failed to create a socket.")
            sys.exit()

        while True:
            try:
                s.connect((self.host, self.port))
            except:
                print("connection failed, trying again in 5 seconds")
                time.sleep(5)
                continue
            break

        while True:
            try:
                if self.message:
                    s.sendall(self.username + ": " + self.message)
                else:
                    break
            except:
                print("message could not be sent")
                break
        s.close()

