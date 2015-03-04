import socket, threading, sys, datetime, struct

class Server(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.IP = '127.0.0.1'
        self.port = 5000
        self.recvd_message = ''

    def setPort(self, port):
        self.port = port

    def getRecvdMsg(self):
        return self.recvd_message

    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind((self.IP, self.port))
        except:
            print("socket could not be bound to the address")
            s.close()

        s.listen(1)

        try:
            conn, addr = s.accept()
        except:
            print("connection failed")
            sys.exit()

        while True:
            data = self.recv_all(conn)
            if "/q" in data:
                break
            else:
                self.recvd_message = "received from " + data + " (" + datetime.datetime.now().strftime('%H:%M') + ")"
        s.close()

    def recv_all(self, socket):
        while True:
            total_len = 0
            total_data = []
            size = sys.maxsize
            size_data = ''
            recv_size = 8192
            while total_len<size:
                sock_data = socket.recv(recv_size)
                if not total_data:
                    if len(sock_data) > 4:
                        size_data += sock_data
                        size = struct.unpack('>i', size_data[:4])[0]
                        recv_size=size
                        if recv_size>524288:recv_size=524288
                        total_data.append(size_data[4:])
                    else:
                        size_data+=sock_data
                else:
                    total_data.append(sock_data)
                total_len=sum([len(i) for i in total_data ])
            return ''.join(total_data)
