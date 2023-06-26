import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Call the clear_screen() function to clear the screen
clear_screen()
