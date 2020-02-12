from pathlib import Path

def seq_read_fasta(filename):
    bodystr = ""
    file_contents = Path(filename).read_text()
    lines = file_contents.split('\n')
    body = lines[1:]
    bodystr = bodystr.join(body).replace(" ", "")
    print(bodystr[0:20])

filename = "U5.txt"
print("DNA file: ", filename)
print("The first 20 bases are: ", seq_read_fasta(filename))


