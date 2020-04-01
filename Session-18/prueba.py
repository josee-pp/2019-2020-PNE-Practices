import termcolor

dicti = [[{'number': '1111', 'type': 'home'}, {'number': '333', 'type': 'office'}], [{'number': '9999-564', 'type': 'home'}], [{'number': '6766534', 'type': 'Dance floor'}, {'number': '333', 'type': 'mobile'}, {'number': '88778', 'type': 'fortnite'}]]

for element in dicti:
    for i, num in enumerate(element):
        termcolor.cprint("  Phone {}:".format(i), 'blue')

        # The element num contains 2 fields: number and type
        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])