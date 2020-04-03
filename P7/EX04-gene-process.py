import http.client
from termcolor import colored
from Seq1 import Seq

gene_dict = {
    "FRAT1": "ENSG00000165879",
    "ADA": "ENSG00000196839",
    "FXN": "ENSG00000165060",
    "RNU6_269P": "ENSG00000212379",
    "MIR633": "ENSG00000207552",
    "TTTY4C": "ENSG00000228296",
    "RBMY2YP": "ENSG00000227633",
    "FGFR3": "ENSG00000068078",
    "KDR": "ENSG00000128052",
    "ANK2": "ENSG00000145362",
}

gene = input("Write the gene name: ")

while True:
    if gene in list(gene_dict.keys()):
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
        lst1 = data1.split()
        descrip = (lst1[1:])[0]
        lst2 = (lst1[1:])[1:]
        seq = (' '.join(map(str, lst2))).replace(' ', '')

        # -- TO PERFORM THE NEXT OPERATIONS WE USE THE SEQ1 CLASS:

        # -- We count the genes:
        s = Seq(seq)
        baselist = ["A", "C", "G", "T"]
        countlist = []
        perclist = []
        # -- We perform the operation for each base in the baselist, and we add each result on a list.
        for base in baselist:
            count = s.count_base(base)
            countlist.append(count)
            percentage = (count / len(seq)) * 100
            perclist.append(f"({round(percentage, 2)} %)")

        # -- Now we extract the most frequent base:
        freqbase = s.processing_genes(baselist)

        # -- Print the info:
        print(f"{colored('Gene', 'green')}: {gene}")
        print(f"{colored('Description', 'green')}: {descrip}")
        print(f"{colored('Total length', 'green')}: {len(seq)}")
        print(f"{colored(baselist[0], 'blue')}: {countlist[0]} {perclist[0]}\n"
              f"{colored(baselist[1], 'blue')}: {countlist[1]} {perclist[1]}\n"
              f"{colored(baselist[2], 'blue')}: {countlist[2]} {perclist[2]}\n"
              f"{colored(baselist[3], 'blue')}: {countlist[3]} {perclist[3]}")
        print(f"{colored('Most frequent base', 'green')}: {freqbase}")
        break

    else:
        print("Gene not found. Try again.")
        gene = input("Write the gene name: ")
