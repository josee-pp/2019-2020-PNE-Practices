import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq
import json

null = " "

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

    global contents

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""



        SERVER = "rest.ensembl.org"
        PARAMS = "?content-type=application/json"


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
        contents = Path('Error.html').read_text()
        code = 200

        # Content type header
        # Both, the error and the main page are in HTML

        try:

            if action == "/":
                contents = Path('main-page.html').read_text()


            elif "/listSpecies" in action:

                limit = arguments[1]

                ENDPOINT = "info/species"

                try:

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
                    response = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response.status} {response.reason}\n")

                    # -- Read the response's body:
                    body = response.read().decode("utf-8")
                    all_species_dict = json.loads(body)
                    all_species_list = []

                    for k, v in all_species_dict.items():
                        if k == "species":
                            for element in v:
                                for k1, v1 in element.items():
                                    if k1 == "display_name":
                                        species = v1
                                        all_species_list.append(species)

                    contents = f"""
                                <!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8" >
                                    <title>List of species</title >
                                </head >
                                <body>
                                <p>The total number of species in ensembl is: {len(all_species_list)}</p>
                                """

                    limit_action = limit.split("=")[0]
                    limit_value = limit.split("=")[1]

                    if limit_action == "limit":
                        if limit_value != "":
                            contents += f"""<p>The number of species you selected are: {limit_value} </p>"""
                            if int(limit_value) > len(all_species_list) or int(limit_value) == 0 or int(limit_value) < 0:
                                contents = f"""<!DOCTYPE html>
                                                <html lang = "en">
                                                <head>
                                                    <meta charset = "utf-8" >
                                                    <title>ERROR</title >
                                                </head>
                                                <body>
                                                <p>The limit you have introduced is out of range. Please, introduce a valid limit value</p>
                                                <a href="/">Main page</a></body></html>"""
                            else:
                                limit_species_list = all_species_list[:(int(limit_value))]
                                contents += f"""<p>The species are: </p>"""
                                for species in limit_species_list:
                                    contents += f"""<p> - {species} </p>"""

                            contents += f"""<a href="/">Main page</a></body></html>"""


                        else:
                            contents += f"""<p>The number of species you selected is null, so all the species are displayed. </p>
                                        <p>The species are: </p>"""
                            for species in all_species_list:
                                contents += f"""<p> - {species} </p>"""
                            contents += f"""<a href="/">Main page</a></body></html>"""

                    else:
                        contents = Path('Error.html').read_text()

                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                 <meta charset = "utf-8" >
                                 <title>ERROR</title >
                                </head>
                                <body>
                                <p>ERROR INVALID VALUE. Introduce an integer value for limit</p>
                                <a href="/">Main page</a></body></html>"""

            elif "/karyotype" in action:

                contents = f"""<!DOCTYPE html>
                            <html lang = "en">
                            <head>
                                <meta charset = "utf-8">
                                 <title> Karyotype </title >
                            </head >
                            <body>
                            """

                get_value = arguments[1]
                species_action = get_value.split("=")[0]
                species_name = get_value.split("=")[1]
                print(species_name)

                ENDPOINT = f"info/assembly/{species_name}"

                try:

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
                    response = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response.status} {response.reason}\n")

                    # -- Read the response's body:
                    body = response.read().decode("utf-8")
                    body = json.loads(body)
                    print(body)


                    for k, v in body.items():

                        if k == "karyotype":

                            if str(v) == "[]":
                                contents = f"""<!DOCTYPE html>
                                            <html lang="en" dir="ltr">
                                            <head>
                                            <meta charset="utf-8">
                                            <title>Error</title>
                                            </head>
                                            <body>
                                            <h1>Error</h1>
                                            <p>Resource not available</p>
                                            <p> The karyotype of this species is not available. </p>
                                            </p>"""

                            else:
                                if species_action == "species":
                                    contents += f"""<p> The names of the chromosomes are:</p>"""
                                    for chromo in v:
                                        contents += f"""<p> - {chromo} </p>"""
                                else:
                                    contents = Path('Error.html').read_text()

                        elif f"{response.status} {response.reason}" == "400 Bad Request":
                            contents = f"""<!DOCTYPE html>
                                            <html lang="en" dir="ltr">
                                            <head>
                                            <meta charset="utf-8">
                                            <title>Error</title>
                                            </head>
                                            <body>
                                            <h1>Error</h1>
                                            <p>Resource not available</p>
                                            <p> This species is not available in ensembl or does not exist. 
                                            """

                        elif f"{response.status} {response.reason}" == "404 Not Found":
                            contents = Path('Error.html').read_text()

                    contents += f"""<p><a href="/">Main page </a></body></html>"""


                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                 <meta charset = "utf-8" >
                                 <title>ERROR</title >
                                </head>
                                <body>
                                <p>ERROR INVALID VALUE</p>
                                <a href="/">Main page</a></body></html>"""


            elif "/chromosomeLength" in action:
                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8">
                                <title> Chromosome Length </title >
                                </head >
                                <body>
                                """

                get_value = arguments[1]

                get_species = get_value.split("&")[0]
                species_name = get_species.split("=")[1]

                get_region_name = get_value.split("&")[1]
                region_name = get_region_name.split("=")[1]


                ENDPOINT = f"info/assembly/{species_name}/{region_name}"

                try:

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
                    response = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response.status} {response.reason}\n")

                    # -- Read the response's body:
                    body = response.read().decode("utf-8")
                    body = json.loads(body)

                    for k,v in body.items():

                        if k == "length":
                            length = str(v)
                            contents += f"""<p> The length of the chromosome is: {length} </p>"""

                        elif f"{response.status} {response.reason}" == "400 Bad Request":
                            contents = f"""<!DOCTYPE html>
                                            <html lang="en" dir="ltr">
                                            <head>
                                            <meta charset="utf-8">
                                            <title>Error</title>
                                            </head>
                                            <body>
                                            <h1>Error</h1>
                                            <p>Resource not available</p>
                                            <p> This species is not available in ensembl or does not exist, 
                                            or the chromosome is invalid. Please, try again. </p>
                                            """

                        elif f"{response.status} {response.reason}" == "404 Not Found":
                            contents = Path('Error.html').read_text()

                    contents += f"""<p><a href="/">Main page </a></body></html>"""

                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                 <meta charset = "utf-8" >
                                 <title>ERROR</title >
                                </head>
                                <body>
                                <p>ERROR INVALID VALUE</p>
                                <a href="/">Main page</a></body></html>"""


            elif "/geneSeq" in action:
                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8">
                                <title> Gene sequence </title >
                                </head >
                                <body>
                                """

                get_value = arguments[1]
                gene_action = get_value.split("=")[0]
                gene_name = get_value.split("=")[1]

                endpoint1 = f"/xrefs/symbol/homo_sapiens/{gene_name}"

                try:

                    # Connect with the server
                    conn = http.client.HTTPConnection(SERVER)

                    # -- Send the request message, using the GET method. We are
                    # -- requesting the main page (/)
                    try:
                        conn.request("GET", endpoint1 + PARAMS)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response message from the server
                    response1 = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response1.status} {response1.reason}\n")

                    # -- Read the response's body:
                    body1 = response1.read().decode("utf-8")
                    body1 = json.loads(body1)
                    dct = body1[0]
                    stable_id = dct["id"]

                    endpoint2 = f"sequence/id/{stable_id}"

                    # Connect with the server
                    conn = http.client.HTTPConnection(SERVER)

                    # -- Send the request message, using the GET method. We are
                    # -- requesting the main page (/)
                    try:
                        conn.request("GET", endpoint2 + PARAMS)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response message from the server
                    response2 = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response2.status} {response2.reason}\n")

                    # -- Read the response's body:
                    body2 = response2.read().decode("utf-8")
                    body2 = json.loads(body2)
                    seq = body2["seq"]

                    if gene_action == "gene":
                        contents += f"""<p> The sequence of {gene_name} is: {seq} </p>"""

                    elif f"{response1.status} {response1.reason}" == "400 Bad Request" or f"{response2.status} {response2.reason}" == "400 Bad Request":
                        contents = f"""<!DOCTYPE html>
                                        <html lang="en" dir="ltr">
                                        <head>
                                        <meta charset="utf-8">
                                        <title>Error</title>
                                        </head>
                                        <body>
                                        <h1>Error</h1>
                                        <p>Resource not available</p>
                                        <p> Invalid gene game. Please, try again. </p>
                                        """

                    elif f"{response1.status} {response1.reason}" == "404 Not Found" or f"{response2.status} {response2.reason}" == "404 Not Found":
                        contents = Path('Error.html').read_text()

                    contents += f"""<p><a href="/">Main page </a></body></html>"""

                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                 <meta charset = "utf-8" >
                                 <title>ERROR</title >
                                </head>
                                <body>
                                <p>ERROR INVALID VALUE</p>
                                <a href="/">Main page</a></body></html>"""

            elif "/geneInfo" in action:

                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8">
                                <title> Gene info </title >
                                </head >
                                <body>
                                """

                get_value = arguments[1]
                gene_action = get_value.split("=")[0]
                gene_name = get_value.split("=")[1]

                endpoint1 = f"/xrefs/symbol/homo_sapiens/{gene_name}"

                try:

                    # Connect with the server
                    conn = http.client.HTTPConnection(SERVER)

                    # -- Send the request message, using the GET method. We are
                    # -- requesting the main page (/)
                    try:
                        conn.request("GET", endpoint1 + PARAMS)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response message from the server
                    response1 = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response1.status} {response1.reason}\n")

                    # -- Read the response's body:
                    body1 = response1.read().decode("utf-8")
                    body1 = json.loads(body1)
                    dct = body1[0]
                    stable_id = dct["id"]

                    endpoint2 = f"lookup/id/{stable_id}"

                    # Connect with the server
                    conn = http.client.HTTPConnection(SERVER)

                    # -- Send the request message, using the GET method. We are
                    # -- requesting the main page (/)
                    try:
                        conn.request("GET", endpoint2 + PARAMS)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response message from the server
                    response2 = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response2.status} {response2.reason}\n")

                    # -- Read the response's body:
                    body2 = response2.read().decode("utf-8")
                    body2 = json.loads(body2)

                    start = body2["start"]
                    end = body2["end"]

                    length = int(end) - int(start)
                    length = str(length)

                    id = body2["id"]
                    chromose = body2["seq_region_name"]

                    if gene_action == "gene":
                        contents += f"""<h1> {gene_name}: </h1>
                                    <p>Start: {start}</p>
                                    <p>End: {end}</p>
                                    <p>Length: {length}</p>
                                    <p>Stable ID: {id}</p>
                                    <p>Chromose: {chromose}</p>
                                    """

                    elif f"{response1.status} {response1.reason}" == "400 Bad Request" or f"{response2.status} {response2.reason}" == "400 Bad Request":
                        contents = f"""<!DOCTYPE html>
                                        <html lang="en" dir="ltr">
                                        <head>
                                        <meta charset="utf-8">
                                        <title>Error</title>
                                        </head>
                                        <body>
                                        <h1>Error</h1>
                                        <p>Resource not available</p>
                                        <p> Invalid gene game. Please, try again. </p>
                                        """

                    elif f"{response1.status} {response1.reason}" == "404 Not Found" or f"{response2.status} {response2.reason}" == "404 Not Found":
                        contents = Path('Error.html').read_text()

                    contents += f"""<p><a href="/">Main page </a></body></html>"""

                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                 <meta charset = "utf-8" >
                                 <title>ERROR</title >
                                </head>
                                <body>
                                <p>ERROR INVALID VALUE</p>
                                <a href="/">Main page</a></body></html>"""

            elif "/geneCalc" in action:

                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8">
                                <title> Gene calc </title >
                                </head >
                                <body>
                                """

                get_value = arguments[1]
                gene_action = get_value.split("=")[0]
                gene_name = get_value.split("=")[1]

                endpoint1 = f"/xrefs/symbol/homo_sapiens/{gene_name}"

                try:

                    # Connect with the server
                    conn = http.client.HTTPConnection(SERVER)

                    # -- Send the request message, using the GET method. We are
                    # -- requesting the main page (/)
                    try:
                        conn.request("GET", endpoint1 + PARAMS)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response message from the server
                    response1 = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response1.status} {response1.reason}\n")

                    # -- Read the response's body:
                    body1 = response1.read().decode("utf-8")
                    body1 = json.loads(body1)
                    dct = body1[0]
                    stable_id = dct["id"]

                    endpoint2 = f"sequence/id/{stable_id}"

                    # Connect with the server
                    conn = http.client.HTTPConnection(SERVER)

                    # -- Send the request message, using the GET method. We are
                    # -- requesting the main page (/)
                    try:
                        conn.request("GET", endpoint2 + PARAMS)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response message from the server
                    response2 = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response2.status} {response2.reason}\n")

                    # -- Read the response's body:
                    body2 = response2.read().decode("utf-8")
                    body2 = json.loads(body2)
                    seq = body2["seq"]

                    s = Seq(seq)

                    length = s.len()

                    baselist = ["A", "C", "G", "T"]
                    countlist = []
                    perclist = []

                    # We perform the operation for each base in the baselist, and we add each result on a list.

                    for base in baselist:
                        count = s.count_base(base)
                        countlist.append(count)
                        percentage = (count / length) * 100
                        perclist.append(f"({round(percentage, 2)} %)")
                    result = f"""
                                <p>Total length: {length}</p>
                                <p>{baselist[0]}: {countlist[0]} {perclist[0]}</p>
                                <p>{baselist[1]}: {countlist[1]} {perclist[1]}</p>
                                <p>{baselist[2]}: {countlist[2]} {perclist[2]}</p>
                                <p>{baselist[3]}: {countlist[3]} {perclist[3]}</p>"""

                    if gene_action == "gene":
                        contents += f"""<h1> {gene_name}: </h1><p>{result}</p>"""

                    elif f"{response1.status} {response1.reason}" == "400 Bad Request" or f"{response2.status} {response2.reason}" == "400 Bad Request":
                        contents = f"""<!DOCTYPE html>
                                        <html lang="en" dir="ltr">
                                        <head>
                                        <meta charset="utf-8">
                                        <title>Error</title>
                                        </head>
                                        <body>
                                        <h1>Error</h1>
                                        <p>Resource not available</p>
                                        <p> Invalid gene game. Please, try again. </p>
                                        """

                    elif f"{response1.status} {response1.reason}" == "404 Not Found" or f"{response2.status} {response2.reason}" == "404 Not Found":
                        contents = Path('Error.html').read_text()

                    contents += f"""<p><a href="/">Main page </a></body></html>"""

                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                                <html lang = "en">
                                                <head>
                                                 <meta charset = "utf-8" >
                                                 <title>ERROR</title >
                                                </head>
                                                <body>
                                                <p>ERROR INVALID VALUE</p>
                                                <a href="/">Main page</a></body></html>"""

            elif action == "/geneList":
                contents = f"""<!DOCTYPE html>
                              <html lang = "en">            
                              <head>  
                              <meta charset = "utf-8"
                              <title> Gene List</title>
                              </head>"""
                endpoint = "overlap/region/human/"
                get_value = arguments[1]
                print(get_value)

        except (KeyError, ValueError, IndexError, TypeError):
            contents = Path('Error.html').read_text()
            contents += f"""<p><a href="/">Main page </a></body></html>"""

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
        print("Stopped by the user")
        httpd.server_close()