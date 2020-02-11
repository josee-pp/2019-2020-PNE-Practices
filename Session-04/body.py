from pathlib import Path

filename = "U5.txt"
file_contents = Path(filename).read_text()

bodystr = " "

lines = file_contents.split('\n')
body = lines[1:]

bodystr = bodystr.join(body)
print(bodystr)

