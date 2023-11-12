RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
for i in range(6):
    if i < 3:
        print(f'{WHITE}{END}')
    else:
        print(f'{RED}{END}')
