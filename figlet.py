import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) <= 1:
    s = input("Input: ")
    random_font = random.randrange(0, len(figlet.getFonts()))
    figlet.setFont(font=figlet.getFonts()[random_font])
    print(f"Output: {(figlet.renderText(s))}")
else:
    s = input("Input: ")
    print(sys.argv[2])
    figlet.setFont(font=sys.argv[2])
    print(f"Output: {(figlet.renderText(s))}")