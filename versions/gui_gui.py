import pyperclip
import sys
import os
from tkinter import *
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library.TextConverter import TextConverter
converter = TextConverter()

def copy_to_clipboard(text):
    pyperclip.copy(text.get())

def add_text(text_input):
    ttk.Label( text=converter.reverse_text(text_input.get())).grid(row=2,column=2)
    ttk.Label( text=converter.text_flip(text_input.get())).grid(row=4,column=2)
    ttk.Label( text=converter.enchant_text(text_input.get())).grid(row=5,column=2)

def add_copy_buttons():
    ttk.Button(root, text="copy", command=partial(copy_to_clipboard, translate_text),).grid(row=2, column=1)

root = Tk()
root.title("Translator")
ico = Image.open('images/icon.ico')
ttk.Label( text="Enter text to translate:").grid(column=0, row=0)
translate_text = Entry(root)
translate_text.grid(row=1, column=0)
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

#
#ttk.Button(frm, text="Enchant text", ).grid(column=2, row=1)
#ttk.Button(frm, text="Change case", ).grid(column=0, row=2)
#ttk.Button(frm, text="Convert to leetspeak", ).grid(column=1, row=2)
#ttk.Button(frm, text="Scramble text", ).grid(column=2, row=2)
#ttk.Button(frm, text="Convert to Pig Latin", ).grid(column=0, row=3)
#ttk.Button(frm, text="Caesar cipher", ).grid(column=1, row=3)
#ttk.Button(frm, text="ASCII art", ).grid(column=2, row=3)
#ttk.Button(frm, text="Border text", ).grid(column=0, row=4)
#ttk.Button(frm, text="Zalgo text", ).grid(column=1, row=4)
#ttk.Button(frm, text="Morse code", ).grid(column=2, row=4)
#ttk.Button(frm, text="Binary text", ).grid(column=0, row=5)
#ttk.Button(frm, text="Shadow text", ).grid(column=1, row=5)
#ttk.Button(frm, text="Scroll text", ).grid(column=2, row=5)
#ttk.Button(frm, text="Generate QR code", ).grid(column=0, row=6)
#ttk.Button(frm, text="Text to emoticons", ).grid(column=1, row=6)
#ttk.Button(frm, text="Nerd mode", ).grid(column=2, row=6)
#ttk.Button(frm, text="exit", ).grid(column=2, row=7)

ttk.Label( text="Reversed text:").grid(row=2,column=0)
ttk.Label( text="Fliped text:").grid(row=4,column=0)
ttk.Label( text="Enchanted text:").grid(row=5,column=0)

ttk.Button(root, text="Submit", command=partial(add_text, translate_text),).grid(row=1, column=1)
add_copy_buttons()
root.mainloop()

def main():
    while True:
        choice = input("Enter your choice (0-18): ")
        text = input("Enter the text to convert: ")
        if choice == '4':
            case = input("Enter 'upper' or 'lower': ")
            result = converter.case_switch(text, case)
            mode = 'case'
        elif choice == '5':
            result = converter.leetspeak(text)
            mode = 'leetspeak'
        elif choice == '6':
            result = converter.scramble_text(text)
            mode = 'scramble'
        elif choice == '7':
            result = converter.piglatin(text)
            mode = 'piglatin'
        elif choice == '8':
            shift = int(input("Enter the shift value: "))
            result = converter.caesar_cipher(text, shift)
            mode = 'caesar'
        elif choice == '9':
            result = converter.ascii_art(text)
            mode = 'ascii'
        elif choice == '10':
            result = converter.border_text(text)
            mode = 'border'
        elif choice == '11':
            result = converter.zalgo_text(text)
            mode = 'zalgo'
        elif choice == '12':
            result = converter.morse_code(text)
            mode = 'morse'
        elif choice == '13':
            result = converter.binary_text(text)
            mode = 'binary'
        elif choice == '14':
            result = converter.text_shadow(text)
            mode = 'shadow'
        elif choice == '15':
            converter.scroll_text(text)
            input("\nPress any key to continue...")
            os.system("clear")
            continue
        elif choice == '16':
            filename = input("Enter the filename for the QR code: ")
            result = converter.qr_code(text, filename)
            mode = 'qr'
        elif choice == '17':
            result = converter.text_to_emoticons(text)
            mode = 'emoticons'
        elif choice == '18':
            result = converter.nerd_mode(text)
            mode = 'nerd'
        else:
            print("Invalid choice. Please try again.")
            continue

        if isinstance(result, dict):
            for key, value in result.items():
                print(f"{key}: {value}")
        elif result:
            print(result)

        if mode != 'qr':
            copy_choice = input("Do you want to copy the result to clipboard? (y/n): ").lower()
            if copy_choice == 'y':
                if isinstance(result, dict):
                    copy_to_clipboard(str(result))
                else:
                    copy_to_clipboard(result)

        if mode != 'qr':
            save_choice = input("Do you want to save the result to a history file? (y/n): ").lower()
            if save_choice == 'y':
                save_message = converter.save_result(result, mode)
                print(save_message)