import socket

# -- Parameters of the server to talk to
IP = "192.168.1.48"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode("Message"))
msg = s.recv(2000)
print("Message from the server: ", msg.decode("utf-8"))
