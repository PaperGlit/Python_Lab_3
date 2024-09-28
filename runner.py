import random
import os
import textwrap
import pyfiglet
from pyfiglet import Figlet


font = 'slant'

try:
    f = Figlet(font=random.choice(pyfiglet.FigletFont.getFonts()), width=os.get_terminal_size().columns)
except OSError:
    f = Figlet(font=random.choice(pyfiglet.FigletFont.getFonts()), width=220)
print(f.renderText('ASCIIFY'))
while True:
    prompt = input("1 - Enter text\n"
          "2 - Change font\n"
          "3 - Current font\n"
          "Your choice: ")
    match prompt:
        case "1":
            text = input("Enter text: ")
            try:
                f = Figlet(font = font, width=os.get_terminal_size().columns)
            except OSError:
                f = Figlet(font=font, width=220)
            print(f.renderText(text))
        case "2":
            new_font = input("Enter new font (or 'font' to see available fonts): ")
            if new_font in pyfiglet.FigletFont.getFonts():
                font = new_font
            elif new_font == "font":
                try:
                    print("Available fonts:\n" + textwrap.fill(", ".join(pyfiglet.FigletFont.getFonts()), width=os.get_terminal_size().columns))
                except OSError:
                    print("Available fonts:\n" + textwrap.fill(", ".join(pyfiglet.FigletFont.getFonts()), width=220))
            else:
                print("Invalid font")
        case "3":
            print("Current font: " + font)
        case _:
            break