import random
import textwrap
import GlobalVariables as Global
import DL.functions.upload_to_file as file_upload
from BLL.classes.ascii import Ascii
from pyfiglet import FigletFont, print_figlet, Figlet, figlet_format


class Console:
    @staticmethod
    def prompt():
        print_figlet("ASCIIFY", font=random.choice(FigletFont.getFonts()),
                     colors=random.choice(Global.colors), width=Ascii.verify_width())
        while True:
            prompt = input("1 - Enter text\n"
                           "2 - Change font\n"
                           "3 - Current font\n"
                           "4 - Change width and height\n"
                           "5 - Change color\n"
                           "Your choice: ")
            match prompt:
                case "1":
                    Console.enter_text()
                case "2":
                    Console.change_font()
                case "3":
                    print("Current font: " + Global.font)
                case "4":
                    Console.change_width_and_height()
                case "5":
                    Console.change_color()
                case _:
                    return

    @staticmethod
    def enter_text():
        text = input("Enter text: ")
        print_figlet(text, font=Global.font, colors=Global.color, width=Ascii.verify_width())
        save_prompt = input("Do you want to save the text? (y/n): ").lower()
        if save_prompt == "y":
            while True:
                file_name = input("Enter file name: ")
                if file_name.strip() != "":
                    ftext = figlet_format(text, font=Global.font, width=Ascii.verify_width())
                    if not file_name.endswith(".txt"):
                        file_name += ".txt"
                    file_upload.write(ftext, file_name)
                    print("Text was uploaded successfully")
                    break
                else:
                    print("Please enter a valid file name")

    @staticmethod
    def change_font():
        new_font = input("Enter the new font you want to choose\n"
                         "You can also use 'font' to see all fonts available or 'random' to choose a random font\n"
                         "Your choice: ")
        if new_font in FigletFont.getFonts():
            Global.font = new_font
        elif new_font.lower() == "font":
            print("Available fonts:\n" + textwrap.fill(", ".join(FigletFont.getFonts()), width=Ascii.verify_width()))
        elif new_font == "random":
            Global.font = random.choice(FigletFont.getFonts())
        else:
            print("Invalid font")

    @staticmethod
    def change_width_and_height():
        while True:
            width_prompt = input("Enter the width of an ASCII art\n"
                      "(any non-positive value will reset it to default values\n"
                      "Your choice: ")
            try:
                width = int(width_prompt)
                Global.width = width
                print("Width changed successfully")
            except ValueError:
                print("Please enter an integer")
                continue
            height_prompt = input("Enter the height of an ASCII art\n"
                                  "(any non-positive value will reset it to default values\n"
                                  "Your choice: ")
            try:
                height = int(height_prompt)
                Global.height = height
                print("Height changed successfully")
                break
            except ValueError:
                print("Please enter an integer")
                continue

    @staticmethod
    def change_color():
        color_prompt = input("Enter the color of your ASCII art:\n"
                             "1 - Red\n"
                             "2 - Green\n"
                             "3 - Blue\n"
                             "4 - Yellow\n"
                             "5 - Cyan\n"
                             "0 - Default\n"
                             "Your choice: ")
        try:
            color = int(color_prompt)
            if color in Global.colors:
                Global.color = Global.colors[color]
                print("Color changed successfully")
            else:
                print("Invalid color choice, please try again.")
        except ValueError:
            print("Please enter an integer")

