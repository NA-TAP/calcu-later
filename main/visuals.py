import os

COLS, LINES = os.get_terminal_size()

def input_bar():
    print(f"\033[{LINES};1H", end="")
    print(f"\033[7m",end="")
    print(" " * (COLS-1),end="")
    print(f"\033[{LINES};1H",end="")
    value = input()
    print(f"\033[{LINES-1};1H",end="")
    print(f"\033[27m",end="")
    print(" " * (COLS-1), end="")
    print(f"\033[1;1H",end="") 

input_bar()
