import socket
from termcolor import colored

class Client:
    def __init__(self, IP, PORT):
        self.IP = IP
        self.PORT = PORT
    def ping(self):
        print("OK!\n")
        return self
    def __str__(self):
        return (f"Connection to SERVER at {self.IP}, PORT: {self.PORT}")
    def talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.IP, self.PORT))
        s.send(str.encode(msg))
        response = s.recv(2048).decode("utf-8")
        s.close()
        return response
    def debug_talk(self, msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.IP, self.PORT))
        msg = colored(msg, "green")
        s.send(str.encode(msg))
        resp = s.recv(2048).decode("utf-8")
        response = colored(resp, "green")
        s.close()
        return response
