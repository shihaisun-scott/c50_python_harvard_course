# Expects zero or two command-line arguments:
# Zero if the user would like to output text in a random font.
# Two if the user would like to output text in a specific font, in which case the first of the two should be 
# -f or --font, and the second of the two should be the name of the font.
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font,
#  the program should exit via sys.exit with an error message.

import sys
import random
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    list_fonts = figlet.getFonts()

    if len(sys.argv) == 1: # random font if 0
        s = input("Input: ")
        figlet.setFont(font = random.choice(list_fonts))
        print(f"Output: {figlet.renderText(s)}")
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in list_fonts:
            s = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print(f"Output: {figlet.renderText(s)}")
        else:
            print("Invalid usage")
            sys.exit()
    else:
        print("Invalid usage")
        sys.exit()

if __name__ == "__main__":
    main()