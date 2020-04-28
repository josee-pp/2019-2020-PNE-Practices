import http.client
from termcolor import colored
from Seq1 import Seq

ID = gene_dict[gene]
SERVER = "rest.ensembl.org"
ENDPOINT = "/sequence/id"
PARAMS = f"/{ID}?content-type=text/x-fasta;type=genomic"
URL = SERVER + ENDPOINT + PARAMS

print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

# Connect with the server
conn = http.client.HTTPConnection(SERVER)

