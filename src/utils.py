from colorama import Fore # colorama is used for coloring the text
import os #os is used to clear the screen

# Clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# global variables
player = ' '
computer = ' '

# Initialize the board
board = [' ' for _ in range(9)]

# Foreground colors are defined here
CYAN        =   Fore.CYAN
LCYAN       =   Fore.LIGHTCYAN_EX
RED         =   Fore.RED
LRED        =   Fore.LIGHTRED_EX
MAGENTA     =   Fore.MAGENTA
LMAGENTA    =   Fore.LIGHTMAGENTA_EX
YELLOW      =   Fore.YELLOW
LYELLOW     =   Fore.LIGHTYELLOW_EX
BLUE        =   Fore.BLUE
LBLUE       =   Fore.LIGHTBLUE_EX
GREEN       =   Fore.GREEN
LGREEN      =   Fore.LIGHTGREEN_EX
RES         =   Fore.RESET
