import pyfiglet
from termcolor import colored
from termcolor import COLORS

# help(pyfiglet)

msg = input("what message do you want to print? ")
color = input("what color? ").upper()

if color not in pyfiglet.COLOR_CODES:
    color = "GREEN"

pyfiglet.print_figlet(msg, 'standard', color)

# another way to do it
color = color.lower()
if color not in COLORS:
    color = "GREEN"

ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color)
print(colored_ascii)

COLORS = dict(
    list(zip([
        'grey',
        'red',
        'green',
        'yellow',
        'blue',
        'magenta',
        'cyan',
        'white',
    ],
        list(range(30, 38))
    ))
)

print(COLORS)
