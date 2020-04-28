import http.client
from termcolor import colored
from Seq1 import Seq

SERVER = "rest.ensembl.org"

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

print(data1)