import socket

IP = "212.128.253.128"
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
s.send(str.encode("Se viene goteoremixxxxxxxxxxxxxxx"))
msg = s.recv(2000)
print("Message from the server: ", msg.decode("utf-8"))
s.close()