import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

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

        # Get the order asked by the user
        order = arguments[0]

        # Content type header
        # Both, the error and the main page are in HTML

        if order == "/":
            contents = Path('form-4.html').read_text()

        # Exercise 1: PING service. Says that the server is alive.
        elif order == "/ping":
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

        # Exercise 2: GET service. Returns the sequence that the user asked for:
        elif order == "/get":

            # We obtain the sequence number by separating the number of the path /get?n=(number):
            seq_number = (arguments[1].split("="))[1]

            # seq_number is the number that the user asked for.
            # Now we use this number to extract the sequence form the list:
            sequence = SEQ_GET[int(seq_number)]
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

        # Exercise 3: GENE service. Returns the gene asked by the user:
        elif order == "/gene":

            # We obtain the gene by separating the number of the path /get?name=(gene):
            gene_name = (arguments[1].split("="))[1]

            # Now we complete the entire filename:
            folder = "C:/Users/Diana/PycharmProjects/2019-2020-PNE-Practices/Session-04/"
            filename = folder + gene_name + ".txt"

            # We use the Seq Class to extract the body of the file:
            s = Seq()
            s1 = Seq(s.read_fasta(filename))
            contents = f"""
                                        <!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                        <meta charset = "utf-8" >
                                            <title>GENE</title >
                                        </head >
                                        <body>
                                        <h1>Gene: {gene_name}:</h1>
                                        <p>{s1}</p>
                                        <a href="/">Main page</a>
                                        </body>
                                        </html>
                                        """

        # Exercise 4: OPERATION service. Returns the requested operation on the sequence introduced.
        elif order == "/operation":
            # We obtain the sequence and the operation from the path:
            data = arguments[1].split('=')
            sequence = (data[1].split('&'))[0]
            operation = data[2]
            # We use the Seq Class to perform the operations:
            s = Seq(sequence)

            # INFO operation:
            if operation == "info":
                baselist = ["A", "C", "G", "T"]
                countlist = []
                perclist = []
                # We perform the operation for each base in the baselist, and we add each result on a list.
                for base in baselist:
                    count = s.count_base(base)
                    countlist.append(count)
                    percentage = (count / len(sequence)) * 100
                    perclist.append(f"({round(percentage, 2)} %)")
                result = f"""
                                        <p>Total length: {len(sequence)}</p>
                                        <p>{baselist[0]}: {countlist[0]} {perclist[0]}</p>
                                        <p>{baselist[1]}: {countlist[1]} {perclist[1]}</p>
                                        <p>{baselist[2]}: {countlist[2]} {perclist[2]}</p>
                                        <p>{baselist[3]}: {countlist[3]} {perclist[3]}</p>"""


            # COMP operation:
            elif operation == "comp":
                result = s.complement()

            # REV operation:
            elif operation == "rev":
                result = s.reverse()

            contents = f"""
                                        <!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                        <meta charset = "utf-8" >
                                            <title>OPERATION</title >
                                        </head >
                                        <body>
                                        <h1>Sequence:</h1>
                                        <p>{sequence}</p>
                                        <h1>Operation:</h1>
                                        <p>{operation}</p>
                                        <h1>Result:</h1>
                                        <p>{result}</p>
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