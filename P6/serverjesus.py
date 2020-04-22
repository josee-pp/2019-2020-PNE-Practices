import http.server
import socketserver
from pathlib import Path
from Seq1 import Seq
# Port
PORT = 8080
# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True
# List of sequences for Get option
Seq_List = ["""AGATCGCGCCACTTCACTGCAGCCTCCGCGAAAGAGCGAAACTCCGTCTCA","TCCTTTCACTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCAC
CCCCACCCA","CAGGAGGCTGAGGCGGGAGGATCGCTTGAGCCCAGGAGGTTGAGGCTGCAGTGAGGTGTG","CACTTGCAAATCATGCAGTTTATGTAGCATTTTCATTTAACACCT
TCTCCCAACCATCTC","CTATGCTAACCCTGTGAACCGTTGCTCGCTTCTCCTTGACATCTGACGGCCTGGCCTTCT"""]
Folder = r"C:\\Users\\jesus.diaz\\PycharmProjects\\2019-2020-PNE-Practices\\Practice 1\\P1\\"
txt = ".txt"
# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties


class TestHandler(http.server.BaseHTTPRequestHandler):
    def do_get(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""
        print(self.requestline)
        # We get the first request line and then the path, goes after /. We get the arguments that go after the ? symbol
        req_line = self.requestline.split(' ')
        path = req_line[1]
        arguments = path.split('?')
        # Action is the first argument
        action = arguments[0]
        contents = Path('error.html').read_text()
        code = 404
        # First we open form-4.html if we don´t specify any action, this is the Index menu
        if action == "/":
            contents = Path('form-4.html').read_text()
            code = 200
        elif action == "/ping":
            contents = """<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Ping </title ></head >
            <body><h2> PING OK!</h2><p> The SEQ2 server in running.... </p><a href="/">Main page</a></body></html>"""
            code = 200
        elif action == "/get":
            # We get the arguments that go after the ? symbol
            get_value = arguments[1]
            # We get the seq index, after we have a couple of elements, the one which we need is the value of the index
            # position of the sequence
            seq_n = get_value.split('?')
            seq_name, index = seq_n[0].split("=")
            index = int(index)
            # Once we have the index we can get our sequence from Seq_List
            seq = Seq_List[index]
            # This is the html code that will show up once we are getting back the sequence we selected
            contents = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Get </title ></head >
            <body><h2> Sequence number {index}</h2><p> {seq} </p><a href="/">Main page</a></body></html>"""
            code = 200
        elif action == "/gene":
            # We get the arguments that go after the ? symbol
            gene_value = arguments[1]
            # After we have a couple of elements, the one which we need is the name of the gene, for reading the file
            # using the specific function from Seq class
            pairs = gene_value.split('?')
            gene_name, gene = pairs[0].split("=")
            # We call Seq class and read the file correspondent to the gene variable, we read the file, get the seq and
            # convert into string
            s = Seq()
            filename = Folder + gene + txt
            seq = Seq(s.read_fasta(filename))
            gene_seq = str(seq)
            # This is the html code that will show up once we are getting back the sequence we selected
            contents = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Gene </title ></head>
            <body><h2> Gene: {gene}</h2><textarea readonly rows="20" cols="80"> {gene_seq} </textarea><br><br>
            <a href="/">Main page</a></body></html>"""
            code = 200
        elif action == "/operation":
            # We get the arguments that go after the ? symbol
            pair = arguments[1]
            # We have a couple of elements, we need the sequence that we previously wrote and the operation to perform
            # that we previously selected
            pairs = pair.split('&')
            seq_name, seq = pairs[0].split("=")
            op_name, op = pairs[1].split("=")
            # Using Seq class we transform the sequence we introduced. According to the operation we selected we will
            # use one function of the class or other
            seq = Seq(seq)
            if op == "rev":
                result = seq.reverse()
            elif op == "comp":
                result = seq.complement()
            else:
                length = seq.len()
                counter_a = seq.count_base('A')
                counter_g = seq.count_base('G')
                counter_c = seq.count_base('C')
                counter_t = seq.count_base('T')
                perc_a = 100 * counter_a / length
                perc_g = 100 * counter_g / length
                perc_c = 100 * counter_c / length
                perc_t = 100 * counter_t / length
                result = f"""<p>Total length: {length}</p><p>A: {counter_a} ({perc_a}%)</p><p>G: {counter_g} ({perc_g}%)
                </p><p>C: {counter_c} ({perc_c}%)</p><p>T: {counter_t} ({perc_t}%)</p>"""

            contents = f"""<!DOCTYPE html><html lang = "en"><head><meta charset = "utf-8" ><title> Operation </title >
            </head ><body><h2> Sequence </h2><p>{seq}</p><h2> Operation: </h2><p>{op}</p><h2> Result: </h2><p>{result}
            </p><br><br><a href="/">Main page</a></body></html>"""
            code = 200

            # Generating the response message
        self.send_response(code)  # -- Status line: OK!

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