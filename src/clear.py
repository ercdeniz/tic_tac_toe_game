import os #os is used to clear the screen

# Clear the screen
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')