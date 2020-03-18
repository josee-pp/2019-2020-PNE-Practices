import http.server
import socketserver
import pathlib

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

def read_fasta(file):
    # -- Open and read the html files
    file_contents = pathlib.Path(file).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        print(self.requestline)

        # ----------------------------------------------------------------------------------

        # Message to send back to the client:

        folder = r"C:/Users/José/PycharmProjects/2019-2020-PNE-Practices/P5/"

        if self.path == "/" or self.path =="/index.html":
            file = "index.html"

        elif "/info/A" in self.path:
            file = "A.html"

        elif "/info/C" in self.path:
            file = "C.html"

        elif "/info/G" in self.path:
            file = "G.html"

        elif "/info/T" in self.path:
            file = "T.html"

        else:
            file = "Error.html"

        contents = read_fasta(folder + file)

        # Generating the response message

        if self.path == "/" or self.path =="/index.html":
            self.send_response(200)  # -- Status line: OK!

        elif "/info/A" or "/info/C" or "/info/G" or "/info/T" in self.path:
            self.send_response(200)  # -- Status line: OK!

        else:
            self.send_response(404)  # -- Status line: ERROR NOT FOUND

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(contents.encode()))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(contents.encode())

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
        print("Stopped by the user")
        httpd.server_close()
