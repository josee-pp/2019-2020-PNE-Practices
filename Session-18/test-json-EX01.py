import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-EX01.json").read_text()

# Create the object person from the json string
person = json.loads(jsonstring)

# Person is now a dictionary. We can read the values
# associated to the fields 'Firstname', 'Lastname' and 'age'

# Print the information on the console, in colors
print()
termcolor.cprint("Name: ", 'green', end="")

# We substract the Firstnames and Lastnames of the JSON:
Firstnames = person["Firstname"]
Lastnames = person["Lastname"]

# Now we complete the entire name of each person:
Names = []
for (firstname,lastname) in zip(Firstnames, Lastnames):
    Names.append(f"{firstname} {lastname}")

# Total people in the database:
NumOfPeople = len(Names)

# We substract the ages:
Ages = person["age"]

# And the phone numbers:
Phones = person["phoneNumber"]

# For each person we print the data:
# (Names.index(i) is the "number" of the person in the list, so i is indeed the person)
for i in Names:
    termcolor.cprint("Name: ", 'green', end="")
    print(i)
    termcolor.cprint("Age: ", 'green', end="")
    print(Ages[Names.index(i)])
    termcolor.cprint("Phone numbers: ", 'green', end="")
    print(len(Phones[Names.index(i)]))

    # Phones is a list of dictionaries, so element is a dictionary:
    for element in Phones:
        # The number (index) of the dictionary must be equal to the number (index) of the person:
        if Names.index(i) == Phones.index(element):
            for a, num in enumerate(element):
                # a is the number of number phone:
                termcolor.cprint("  Phone {}:".format(a), 'blue')
                # The element num contains 2 fields: number and type
                termcolor.cprint("    Type: ", 'red', end='')
                print(num['type'])
                termcolor.cprint("    Number: ", 'red', end='')
                print(num['number'])
            print()

