from Client0 import Client

PRACTICE = 2
EXERCISE = 3

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "212.128.253.1"
PORT = 8080

# -- Create a client object
c = Client(IP, PORT)

# -- Testing the talk function:
print("Sending a message to the server...")
response = c.talk("Testing!!!")
print(f"Response: {response}")
