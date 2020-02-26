class Client:
    def __init__(self, IP, PORT):
        print("OK!")
        self.IP = IP
        self.PORT = PORT

    def ping(self):
        return self
    def __str__(self):
        return (f"Connection to SERVER at {self.IP}, PORT: {self.PORT}")




