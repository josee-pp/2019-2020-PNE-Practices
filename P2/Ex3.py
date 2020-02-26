from Client0 import Client

PRACTICE = 2
EXERCISE = 1

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "192.168.124.179"
PORT = 8080

c = Client(IP, PORT)


print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
