import pyperclip
import pygame
import random
from art import text2art
import sys
import time
import qrcode
from collections import Counter


def flipUD(text):
    flip_map = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!?\"'()[]{}",
        "ɐqɔpǝɟɓɥᴉſʞlɯuodbɹsʇnʌʍxʎz∀ꓭƆꓷƎℲꓨHIſꓘ⅃WNOꓒΌꓤSꓕꓵΛM⅄Z⇂ᘕԐત૨୧L8მ0·ˋ¡¿\\„,)(][}{"
    )

    return text.translate(flip_map)[::-1]


def reverse_text(text):
    reversed_text = text[::-1]
    print("The result is: ", reversed_text)
    pyperclip.copy(reversed_text)
    with open('reverse_history.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(reversed_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called reverse_history.txt, if it's easier to copy from there.")


def text_flip(text):
    converted_text = flipUD(text)
    print("The result is: ", converted_text)
    pyperclip.copy(converted_text)
    with open('flip_history.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(converted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called flip_history.txt, if it's easier to copy from there.")


def enchant_text(text):
    enchanted_text = str.maketrans(
        "abcdefghijklmnoqrstuvwzABCDEFGHIJKLMNOQRSTUVWZ1234567890.,!?\"'()[]{}",
        "ᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹ᑑ∷ᓭℸ⚍⍊∴Λᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹ᑑ∷ᓭℸ⚍⍊∴Λ1234567890.,!?\"'()[]{}"
    )
    enchanted_text = text.translate(enchanted_text)
    enchanted_text = str(enchanted_text).replace(
        'p', '!¡').replace(
        'P', '!¡').replace(
            'y', '||').replace(
                'Y', '||').replace(
                    'x', ' ̇/').replace(
                        'X', ' ̇/')
    print("The result is: ", enchanted_text)
    pyperclip.copy(enchanted_text)
    with open('enchant_history.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(enchanted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called enchant_history.txt, if it's easier to copy from there.")


def case_switch(case, text):
    if case == 'U':
        converted_text = text.upper()
    elif case == 'L':
        converted_text = text.lower()
    else:
        print("Something went wrong.")
    print(f"The result is: {converted_text}")
    pyperclip.copy(converted_text)
    with open('case_history.txt', 'a') as f:
        f.write('\n')
        f.write(converted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called case_history.txt, if it's easier to copy from there.")


def leetspeak(text):
    leet_dict = {'a': '4', 'e': '3', 'l': '1', 'o': '0', 't': '7'}
    converted_text = ''.join(leet_dict.get(char, char) for char in text.lower())
    print("The result is: ", converted_text)
    pyperclip.copy(converted_text)
    with open('leetspeak_history.txt', 'a') as f:
        f.write('\n')
        f.write(converted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called leetspeak_history.txt, if it's easier to copy from there.")


def scramble_text(text):
    scrambled_text = ''.join(random.sample(text, len(text)))
    print("The result is: ", scrambled_text)
    pyperclip.copy(scrambled_text)
    with open('scramble_history.txt', 'a') as f:
        f.write('\n')
        f.write(scrambled_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called scramble_history.txt, if it's easier to copy from there.")


def piglatin(text):
    vowels = "aeiouAEIOU"
    if text[0] in vowels:
        piglatin_text = text + "way"
    else:
        piglatin_text = text[1:] + text[0] + "ay"
    print("The result is: ", piglatin_text)
    pyperclip.copy(piglatin_text)
    with open('piglatin_history.txt', 'a') as f:
        f.write('\n')
        f.write(piglatin_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called piglatin_history.txt, if it's easier to copy from there.")


def caesar_cipher(text, shift):
    encrypted = []
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            encrypted.append(chr((ord(char) - shift_amount + shift) % 26 + shift_amount))
        else:
            encrypted.append(char)
    encrypted_text = ''.join(encrypted)
    print("The result is: ", encrypted_text)
    pyperclip.copy(encrypted_text)
    with open('caesar_history.txt', 'a') as f:
        f.write('\n')
        f.write(encrypted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called caesar_history.txt, if it's easier to copy from there.")


def ascii_art(text):
    ascii_text = text2art(text)
    print("The result is: ", ascii_text)
    pyperclip.copy(ascii_text)
    with open('ascii_history.txt', 'a') as f:
        f.write('\n')
        f.write(ascii_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called ascii_history.txt, if it's easier to copy from there.")


def border_text(text):
    border_text = text2art(text, font='block')
    print("The result is: ", border_text)
    pyperclip.copy(border_text)
    with open('border_history.txt', 'a') as f:
        f.write('\n')
        f.write(border_text)
        f.write('\n')
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called border_history.txt, if it's easier to copy from there.")


def zalgo_text(text):
    zalgo_chars = ['̍', '̎', '̄', '̅', '̿', '̑', '̆', '̐', '͒', '͗', '͑', '̇', '̈', '̊', '͂', '̓', '̈', '͊', '͋', '͌', '̃', '̂', '̌', '͐', '̀', '́', '̋', '̏', '̒', '̓', '̔', '̽', '̉', 'ͣ', 'ͤ', 'ͥ', 'ͦ', 'ͧ', 'ͨ', 'ͩ', 'ͪ', 'ͫ', 'ͬ', 'ͭ', 'ͮ', 'ͯ', '̾', '͛', '͆', '̚']
    zalgo_text = ''.join(random.choice(zalgo_chars) + char for char in text)
    print("The result is: ", zalgo_text)
    pyperclip.copy(zalgo_text)
    with open('zalgo_history.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(zalgo_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called zalgo_history.txt, if it's easier to copy from there.")


def morse_code(text):
    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
        ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }
    morse_code = ' '.join(MORSE_CODE_DICT.get(char.upper(), '') for char in text)
    print("The result is: ", morse_code)
    pyperclip.copy(morse_code)
    with open('morse_history.txt', 'a') as f:
        f.write('\n')
        f.write(morse_code)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called morse_history.txt, if it's easier to copy from there.")


def binary_text(text):
    binary_text = ' '.join(format(ord(char), '08b') for char in text)
    print("The result is: ", binary_text)
    pyperclip.copy(binary_text)
    with open('binary_history.txt', 'a') as f:
        f.write('\n')
        f.write(binary_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called binary_history.txt, if it's easier to copy from there.")


def text_shadow(text):
    shadow = '\n'.join(' ' * offset + line for line in text.split('\n'))
    shadowed_text =  f"{text}\n{shadow}"
    print("The result is: ", shadowed_text)
    pyperclip.copy(shadowed_text)
    with open('shadow_history.txt', 'a') as f:
        f.write('\n')
        f.write(shadowed_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called shadow_history.txt, if it's easier to copy from there.")


def scroll_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img.save(f"{filename}.png")
    print("QR code saved as ", filename, ".png")


def text_to_emoticons(text):
    emoticon_dict = {'hello': '👋', 'world': '🌍'}
    words = text.split()
    emojis = ' '.join(emoticon_dict.get(word.lower(), word) for word in words)
    print("The result is: ", emojis)
    pyperclip.copy(emojis)
    with open('emoticons_history.txt', 'a') as f:
        f.write('\n')
        f.write(emojis)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called emoticons_history.txt, if it's easier to copy from there.")


def nerd_mode(text):
    word_count = len(text.split())
    char_count = len(text)
    char_frequency = Counter(text)

    print(f"Word Count: {word_count}")
    print(f"Character Count: {char_count}")
    print(f"Character Frequency: {char_frequency}")


def prompt_redo():
    redo = str(input("Continue? (y/n) "))
    if redo == "y":
        return "redo"
    elif redo == "n":
        return "stop"
has_gui=input("do you want this to be in the teminal (1) or have a gui (2)")

if str(has_gui)=="2":
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    programIcon = pygame.image.load('images/icon.ico')
    pygame.display.set_icon(programIcon)
    pygame.display.set_caption('translator')

while str(has_gui) != "2":
    text_input = str(input("Input the string you need to convert here: "))
    print("Modes:\nForce into full upper/lowercase (CASE) \nFlip text upside-down (FLIP)\nConvert text to the Standard Galactic Alphabet, aka Minecraft enchanting table speak (ENCHANT)\nReverse text in a string (REVERSE)\nConvert text to leetspeak (LEETSPEAK)\nRandomly scramble the text (SCRAMBLE)\nAdd Pig Latin to the text (PIGLATIN)\nShift your text into Ceasar Cipher (CAESAR)\nASCII Art your text (ASCII)\nAdd a border to your text (BORDER)\nAdd Zalgo decor to your text (ZALGO)\nConvert text to Morse code (MORSE)\nConvert to binary (BINARY)\nAdd shadows to your text (SHADOW)\nConvert text to emoticons (EMOTICONS)\nExtra modes (EXTRA)\nExit (EXIT)")
    mode = str(input("\nWhich mode would you like to use? "))

    if mode.lower() == "case":
        casing = int(input("Type U for uppercase or L for lowercase. "))
        case_switch(casing, text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "flip":
        text_flip(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "zalgo":
        zalgo_text(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "enchant":
        enchant_text(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "reverse":
        reverse_text(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "leetspeak":
        leetspeak(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "piglatin":
        piglatin(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "scramble":
        scramble_text(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "caesar":
        caesar_cipher(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "ascii":
        ascii_art(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "border":
        border_text(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "morse":
        morse_code(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "binary":
        binary_text(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "shadow":
        text_shadow(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "scroll":
        scroll_text(text_input)
        restart = prompt_redo()
        if restart == "stop":
            break

    elif mode.lower() == "extra":
        print("\nModes:\nConvert text to emoticons (EMOTICONS)\nMake your text into QR Code (QR)\nScroll text (SCROLL)\nNerd mode (NERD)\nBack (BACK)\nExit (EXIT)")
        extra_mode = str(input("Which mode would you like to use? "))
        if extra_mode.lower() == "emoticons":
            text_to_emoticons(text_input)
            restart = prompt_redo()
            if restart == "stop":
                break
        elif extra_mode.lower() == "qr":
            filename = str(input("What would you like to name the QR code? "))
            qr_code(text_input, filename)
            restart = prompt_redo()
            if restart == "stop":
                break
        elif extra_mode.lower() == "scroll":
            scroll_text(text_input)
            restart = prompt_redo()
            if restart == "stop":
                break
        elif extra_mode.lower() == "nerd":
            nerd_mode(text_input)
            restart = prompt_redo()
            if restart == "stop":
                break

        elif extra_mode.lower() == "back":
            continue

        elif extra_mode.lower() == "exit":
            break

    elif mode.lower() == "exit":
        break

    else:
        print("Couldn't understand you. Did you perhaps misspell the mode?")
