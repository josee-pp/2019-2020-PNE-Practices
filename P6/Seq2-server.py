import http.server
import socketserver
import termcolor
from pathlib import Path

# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

# Define the list of sequences for the EX-02:
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

        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        # Analize the requestline:
        reqline = self.requestline.split(' ')

        # Get the path that always starts with "/"
        path = reqline[1]

        # Read the arguments
        arguments = path.split('?')

        # Get the verb. It is the first argument
        verb = arguments[0]

        # -- Content type header
        # -- Both, the error and the main page are in HTML

        if verb == "/":
            contents = Path('form-2.html').read_text()

        # Exercise 1: PING service. Says that the server is alive.
        elif verb == "/ping":
            contents = f"""
                                    <!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                    <meta charset = "utf-8" >
                                        <title>PING</title >
                                    </head >
                                    <body>
                                    <h1>PING OK!</h1>
                                    <p>The SEQ2 server in running...</p>
                                    <a href="/">Main page</a>
                                    </body>
                                    </html>
                                    """

        # Exercise 2: Returns the sequence that the user asked for:
        elif verb == "/get":
            # We obtain the sequence number by separating the number of the path /get?n=(number):
            seq_number = (arguments[1].split("="))[1]
            sequence = SEQ_GET[seq_number]
            contents = f"""
                                    <!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                    <meta charset = "utf-8" >
                                        <title>GET</title >
                                    </head >
                                    <body>
                                    <h1>Sequence number {seq_number}:</h1>
                                    <p>{sequence}</p>
                                    <a href="/">Main page</a>
                                    </body>
                                    </html>
                                    """


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