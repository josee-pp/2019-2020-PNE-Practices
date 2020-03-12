from pathlib import Path
from Client0 import Client
from Seq1 import Seq

PORT = 8080
IP = "192.168.1.48"

c = Client(IP, PORT)

msg = input("Enter message: ")

response = client.debug_talk(msg)

