import Server, Client, threading
from kivy.app import App

from kivy.uix.boxlayout import BoxLayout


class Fenster(BoxLayout):

    def server(self):
        server = Server.Server().run()

        while True:
            if server.recvd_message:
                self.ids.msg_output.text = server.recvd_message
                server.recvd_message = ''

    def connect(self):
        self.port = int(self.ids.port.text)
        self.ip = self.ids.ip.text
        self.user = self.ids.user.text

        t = threading.Thread(target = self.server)
        t.start()


    def send(self):
        message = self.ids.msg_input.text
        Client.Client('127.0.0.1', 5000, 'timo', message)

class ChatApp(App):

    def build(self):
        return Fenster()

