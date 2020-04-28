import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
data = json.loads(data1)

firstnames = data["Firstname"]
lastnames = data["Lastname"]
fullnames = [i + f" {j}" for i, j in zip(firstnames, lastnames)]

ages = data["age"]
numberslist = data["phoneNumber"]

print("Total people on the data base: ", len(fullnames))
for person in fullnames:
    index = fullnames.index(person)
    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person)
    termcolor.cprint("Age: ", 'green', end="")
    print(ages[index])
    termcolor.cprint("Phonenumbers: ", 'green', end="")
    personnumbers = numberslist[index]
    print(len(personnumbers))
    for i,num in enumerate(personnumbers):
        termcolor.cprint(f"  Phone {i}: ", "blue")
        termcolor.cprint("      Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("      Number: ", 'red', end='')
        print(num['number'])

