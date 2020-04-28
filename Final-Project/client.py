import http.client
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

        # Define the contents and the code:
        contents = Path('Error.html').read_text()
        code = 200

        try:

            # Main page:
            if action == "/":
                contents = Path('main-page.html').read_text()

            # - - - BASIC LEVEL - - -

            # List Species: List the names of all the species available in the database. The limit parameter (optional)
            # indicates the maximum number of species to show. If it is not specified, all the species will be listed:

            elif "/listSpecies" in action:

                # We extract the limit number entered by the user from the arguments:
                limit = arguments[1]

                # This endpoint lists all available species, their aliases, available adaptor groups and data release.
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

                    # -- We convert the body from string to dictionary:
                    all_species_dict = json.loads(body)

                    # -- We define the list of all species:
                    all_species_list = []

                    # -- We extract the display name of each species from the dictionary. Each species is a element of
                    # -- a list, that is the value of a key called species.

                    for k, v in all_species_dict.items():
                        if k == "species":
                            for element in v:
                                for k1, v1 in element.items():
                                    if k1 == "display_name":
                                        species = v1

                                        # -- We add each species to the list:
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

                    # From limit, we extract the order and the value entered by the user:
                    limit_action = limit.split("=")[0]
                    limit_value = limit.split("=")[1]

                    if limit_action == "limit":

                        # In case the user enters a limit value:
                        if limit_value != "":
                            contents += f"""<p>The number of species you selected are: {limit_value} </p>"""

                            # Invalid limit values:
                            if int(limit_value) > len(all_species_list) or int(limit_value) == 0 or int(
                                    limit_value) < 0:
                                contents = f"""<!DOCTYPE html>
                                                    <html lang = "en">
                                                    <head>
                                                        <meta charset = "utf-8" >
                                                        <title>ERROR</title >
                                                    </head>
                                                    <body>
                                                    <p>The limit you have introduced is out of range. Please, introduce a valid limit value</p>
                                                    </body></html>"""
                            else:
                                # We extract the first n species of the list, being n the limit ordered by the user.
                                limit_species_list = all_species_list[:(int(limit_value))]
                                contents += f"""<p>The species are: </p>"""
                                # The species are printed one by one:
                                for species in limit_species_list:
                                    contents += f"""<p> - {species} </p>"""

                            contents += f"""<a href="/">Main page</a></body></html>"""

                        # In case the user does not enter any limit number, all the species will be displayed:
                        else:
                            contents += f"""<p>The number of species you selected is null, so all the species are displayed. </p>
                                        <p>The species are: </p>"""

                            # The species are printed one by one:
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

            # Karyotype: Return information about the karyotype of a specie: The name (usually a number) of all the
            # chromosomes:

            elif "/karyotype" in action:

                contents = f"""<!DOCTYPE html>
                            <html lang = "en">
                            <head>
                                <meta charset = "utf-8">
                                 <title> Karyotype </title >
                            </head >
                            <body>
                            """

                # We extract the species entered by the user from the arguments:
                get_value = arguments[1]

                # We obtain the action and the name of the species:
                species_action = get_value.split("=")[0]
                species_name = get_value.split("=")[1]

                # Now we can define the endpoint. This one list the currently available assemblies for a species, along
                # with toplevel sequences, chromosomes and cytogenetic bands.
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

                    # -- We convert the string to a dictionary:
                    body = json.loads(body)

                    # -- We extract the karyotype of the demanded species from the dictionary. Karyotype is a key from
                    # -- the dictionary.
                    for k, v in body.items():

                        if k == "karyotype":

                            # In case the entered species has no karotype info in ensembl:
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
                                    # V is the list of chromosomes, it is, the karyotype. Each chromosome is printed
                                    # one by one:
                                    for chromo in v:
                                        contents += f"""<p> - {chromo} </p>"""
                                else:
                                    contents = Path('Error.html').read_text()

                        # The entered species does not exist in ensembl:
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
                                            <p> This species is not available in ensembl or does not exist.</p>. 
                                            """

                        # The user did not enter the name of the species:
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

            # Chromosome Length: Return the Length of the chromosome named "chromo" of the given species.
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

                # get_value give us:

                # 1.- The name of the species:
                get_species = get_value.split("&")[0]
                species_name = get_species.split("=")[1]

                # 2.- The chromosome:
                get_region_name = get_value.split("&")[1]
                region_name = get_region_name.split("=")[1]

                # Now we can define the endpoint. This one Returns information about the specified toplevel sequence
                # region for the given species.
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

                    # -- We convert the string into a dictionary:
                    body = json.loads(body)

                    # For k = keys, v = values.
                    for k, v in body.items():

                        if k == "length":
                            length = str(v)
                            contents += f"""<p> The length of the chromosome is: {length} </p>"""

                        # The species does not exist or the chromosome is invalid.
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

                        # The user did not enter any info.
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

            # - - - MEDIUM LEVEL - - -

            # geneSeq: Return the sequence of a given human gene
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

                # We extract the gene name from the arguments:
                gene_name = get_value.split("=")[1]

                # We define our first endpoint to obtain the stable ID of the gene. This endpoint receives the species
                # (in this case, human) and returns info about that gene, in which we can find the stable ID:
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

                    # -- We convert the string to a dictionary:
                    body1 = json.loads(body1)

                    # -- The first element of body1 has the stable ID inside:
                    dct = body1[0]

                    # -- We extract it:
                    stable_id = dct["id"]

                    # -- We define our second endpoint. This one takes a stable ID and returns the complete sequence
                    # -- of that gene.
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

                    # -- We convert the string to a dictionary:
                    body2 = json.loads(body2)

                    # -- We extract the full sequence:
                    seq = body2["seq"]

                    # -- The gene given by the user is correct:
                    if f"{response1.status} {response1.reason}" == "200 OK" or f"{response2.status} {response2.reason}" == "200 OK":
                        contents += f"""<p> The sequence of {gene_name} is: {seq} </p>"""

                    # -- The gene given is incorrect, does not exist or is not available in ensembl:
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

                    # -- The user entered a blank space:
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

            # geneInfo: Return information about a human gene: start, end, length, ID and chromose.
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

                # We obtain the name of the gene from the arguments:
                gene_name = get_value.split("=")[1]

                # And now we can define our first endpoint. Is the same as the previous function: we will obtain the
                # stable ID:
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

                    # -- We convert the string to a dictionary:
                    body1 = json.loads(body1)

                    # -- The first element of the dictionary has the stable ID
                    dct = body1[0]
                    stable_id = dct["id"]

                    # -- This endpoint give us the requested info as a dictionary:
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

                    # -- We convert the string into a dictionary:
                    body2 = json.loads(body2)

                    # -- We extract the info (values) by the name of the keys:
                    start = body2["start"]
                    end = body2["end"]

                    length = int(end) - int(start)
                    length = str(length)

                    id = body2["id"]
                    chromose = body2["seq_region_name"]

                    # The info that the user has entered is correct:
                    if f"{response1.status} {response1.reason}" == "200 OK" or f"{response2.status} {response2.reason}" == "200 OK":
                        contents += f"""<h1> {gene_name}: </h1>
                                    <p>Start: {start}</p>
                                    <p>End: {end}</p>
                                    <p>Length: {length}</p>
                                    <p>Stable ID: {id}</p>
                                    <p>Chromose: {chromose}</p>
                                    """

                    # The gene name is incorrect, does not exist or is not available in ensembl:
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

                    # The user entered a blank space:
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

            # geneCalc: Performs some calculations on the given human gene and returns the total length and the
            # percentage of all its bases:
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

                # We obtain the gene name:
                gene_name = get_value.split("=")[1]

                # We obtain the stable ID:
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

                    # -- We convert the string into a dictionary:
                    body1 = json.loads(body1)

                    dct = body1[0]
                    stable_id = dct["id"]

                    # We obtain the entire sequence:
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

                    # We use the Seq class to perform operations:
                    s = Seq(seq)

                    length = s.len()

                    baselist = ["A", "C", "G", "T"]
                    countlist = []
                    perclist = []

                    # We perform the operation for each base in the baselist, and we add each result on a list.
                    # count_base(base) counts each base:

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

                    # The gene given by the user is correct:
                    if f"{response1.status} {response1.reason}" == "200 OK" or f"{response2.status} {response2.reason}" == "200 OK":
                        contents += f"""<h1> {gene_name}: </h1><p>{result}</p>"""

                    # The gene does not exist, is incorrect or is not available in ensembl:
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

                    # The user entered a blank space:
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

            # geneList: Return the names of the genes located in a chromosome from the start to end positions.
            elif action == "/geneList":
                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <title> Gene list </title >
                                <meta charset = "utf-8">
                                </head >
                                <body>
                                <h1> List of genes: </h1>
                                """

                get_value = arguments[1]

                # First we split get_value:
                get_chromo = get_value.split('&')[0]
                get_start = get_value.split('&')[1]
                get_end = get_value.split('&')[2]

                # Then we obtain the values entered by the user:
                chromo = get_chromo.split("=")[1]
                start = get_start.split("=")[1]
                end = get_end.split("=")[1]

                # This endpoint give us all the genes in that chromo, between start and end (human).
                endpoint = f"overlap/region/human/{chromo}:{start}-{end}"
                parameters = '?feature=gene;content-type=application/json'

                try:

                    # Connect with the server
                    conn = http.client.HTTPConnection(SERVER)

                    # -- Send the request message, using the GET method. We are
                    # -- requesting the main page (/)
                    try:
                        conn.request("GET", endpoint + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()

                    # -- Read the response message from the server
                    response = conn.getresponse()

                    # -- Print the status line
                    print(f"Response received!: {response.status} {response.reason}\n")

                    # -- Read the response's body:
                    body = response.read().decode("utf-8")

                    # -- This is a list of dictionaries, and each dictionary is a gene. Each dictionary has a key called
                    # -- "external_name", which is the gene name we want to obtain:

                    body = json.loads(body)

                    # The data entered by the user is correct:
                    if f"{response.status} {response.reason}" == "200 OK":
                        for gene in body:
                            contents += f"""<p> - {gene["external_name"]} </p>"""

                    # The data is incorrect or does not match which the available data in ensembl:
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

                    # The user entered blank spaces:
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