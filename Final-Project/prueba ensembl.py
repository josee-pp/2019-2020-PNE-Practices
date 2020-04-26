import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Define the list of sequences for GET option:
SEQ_GET = [
    "ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA",
    "AAAAACATTAATCTGTGGCCTTTCTTTGCCATTTCCAACTCTGCCACCTCCATCGAACGA",
    "CAAGGTCCCCTTCTTCCTTTCCATTCCCGTCAGCTTCATTTCCCTAATCTCCGTACAAAT",
    "CCCTAGCCTGACTCCCTTTCCTTTCCATCCTCACCAGACGCCCGCATGCCGGACCTCAAA",
    "AGCGCAAACGCTAAAAACCGGTTGAGTTGACGCACGGAGAGAAGGGGTGTGTGGGTGGGT",
]

# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        SERVER = "rest.ensembl.org"
        ENDPOINT = "info/species"
        PARAMS = "?content-type=application/json"
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
        all_species_dict = r1.read().decode("utf-8")
        print(all_species_dict)

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the requestline:
        reqline = self.requestline.split(' ')

        # Get the path that always starts with "/"
        path = reqline[1]

        # Read the arguments
        arguments = path.split('?')

        # Get the order asked by the user
        action = arguments[0]

        # Content type header
        # Both, the error and the main page are in HTML

        if action == "/":
            contents = Path('main-page.html').read_text()

        else:
            contents = Path('Error.html').read_text()

        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return

# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()