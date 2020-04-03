import http.client
from termcolor import colored

SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
PARAMS = "/ENSG00000207552?content-type=text/x-fasta;type=genomic"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", ENDPOINT + PARAMS)
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- We extract the description and the sequence:
lst = data1.split(' ')
data = lst[1]
descrip = data.split()[0]
seq = data.split()[1]

# -- Print the info:

print(f"{colored('Gene', 'green')}: MIR633")
print(f"{colored('Description', 'green')}: {descrip}")
print(f"{colored('Bases', 'green')}: {seq}")


