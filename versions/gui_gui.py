import pyperclip
import os
import sys
from tkinter import *
from tkinter import ttk
from functools import partial
from PIL import Image, ImageTk
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library.TextConverter import TextConverter
converter = TextConverter()
text_lable_column=0
copy_button_column=1
text_output_column=2
dir = os.path.dirname(__file__)

def copy_to_clipboard(text):
    pyperclip.copy(text['text'])

def add_text(*args):
    new_text = translate_text.get()
    x_size=int(8.5*len(new_text)+240)
    root.geometry(f"{x_size}x{350}")
    reversed_text['text'] = converter.reverse_text(new_text)
    flipped_text['text'] = converter.text_flip(new_text)
    enchanted_text['text'] = converter.enchant_text(new_text)
    capitalized_text['text'] = converter.case_switch(new_text, "upper")
    lowercased_text['text'] = converter.case_switch(new_text, "lower")
    leetspeak_text['text'] = converter.leetspeak(new_text)
    scrambled_text['text'] = converter.scramble_text(new_text)
    piglatin_text['text'] = converter.piglatin(new_text)
    zalgo_text['text'] = converter.zalgo_text(new_text)
    emoticons_text['text'] = converter.text_to_emoticons(new_text)

def add_copy_buttons():
    ttk.Button(root, command=partial(copy_to_clipboard, reversed_text), image = copy_icon).grid(sticky = W, row=1, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, flipped_text), image = copy_icon).grid(sticky = W, row=2, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, enchanted_text), image = copy_icon).grid(sticky = W, row=3, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, capitalized_text), image = copy_icon).grid(sticky = W, row=4, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, capitalized_text), image = copy_icon).grid(sticky = W, row=5, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, leetspeak_text), image = copy_icon).grid(sticky = W, row=6, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, scrambled_text), image = copy_icon).grid(sticky = W, row=7, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, piglatin_text), image = copy_icon).grid(sticky = W, row=8, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, zalgo_text), image = copy_icon).grid(sticky = W, row=9, column=copy_button_column)
    ttk.Button(root, command=partial(copy_to_clipboard, emoticons_text), image = copy_icon).grid(sticky = W, row=10, column=copy_button_column)

root = Tk()
root.title("Translator")
ico = Image.open(os.path.join(dir,'./images/icon.ico'))
photo = ImageTk.PhotoImage(ico)
copy_icon = Image.open(os.path.join(dir,'./images/content_copy.png'))
copy_icon = ImageTk.PhotoImage(copy_icon)
root.wm_iconphoto(False, photo)
root.geometry("240x350")

translate_text = StringVar()
translate_text.trace_add("write", add_text)
input_widget = ttk.Entry(root, textvariable=translate_text)
input_widget.grid(row=0, column=0, columnspan=2)

ttk.Label(text="Reversed:").grid(row=1,column=text_lable_column)
reversed_text = ttk.Label(justify="left")
reversed_text.grid(row=1, column=text_output_column, sticky = W)

ttk.Label(text="Flipped:").grid(row=2,column=text_lable_column)
flipped_text = ttk.Label(justify="left")
flipped_text.grid(row=2, column=text_output_column, sticky = W)

ttk.Label(text="Enchanted:").grid(row=3,column=text_lable_column)
enchanted_text = ttk.Label(justify="left")
enchanted_text.grid(row=3, column=text_output_column, sticky = W)

ttk.Label(text="Capitalized:").grid(row=4,column=text_lable_column)
capitalized_text = ttk.Label(justify="left")
capitalized_text.grid(row=4, column=text_output_column, sticky = W)

ttk.Label(text="Lowercased:").grid(row=5,column=text_lable_column)
lowercased_text = ttk.Label(justify="left")
lowercased_text.grid(row=5, column=text_output_column, sticky = W)

ttk.Label(text="Leetspeak:").grid(row=6,column=text_lable_column)
leetspeak_text = ttk.Label(justify="left")
leetspeak_text.grid(row=6, column=text_output_column, sticky = W)

ttk.Label(text="Scrambled:").grid(row=7,column=text_lable_column)
scrambled_text = ttk.Label(justify="left")
scrambled_text.grid(row=7, column=text_output_column, sticky = W)

ttk.Label(text="piglatin:").grid(row=8,column=text_lable_column)
piglatin_text = ttk.Label(justify="left")
piglatin_text.grid(row=8, column=text_output_column, sticky = W)

ttk.Label(text="zalgo:").grid(row=9,column=text_lable_column)
zalgo_text = ttk.Label(justify="left")
zalgo_text.grid(row=9, column=text_output_column, sticky = W)

ttk.Label(text="emoticons:").grid(row=10,column=text_lable_column)
emoticons_text = ttk.Label(justify="left")
emoticons_text.grid(row=10, column=text_output_column, sticky = W)

add_copy_buttons()
root.mainloop()
