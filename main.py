import pyperclip
import random


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


def prompt_redo():
    redo = str(input("Continue? (y/n) "))
    if redo == "y":
        return "redo"
    elif redo == "n":
        return "stop"


while True:
    mode = str(input("Modes:\nForce into full upper/lowercase (CASE) \nFlip text upside-down (FLIP)\nConvert text to the Standard Galactic Alphabet, aka Minecraft enchanting table speak (ENCHANT)\nReverse text in a string (REVERSE)\nConvert text to leetspeak (LEETSPEAK)\nRandomly scramble the text (SCRAMBLE)\nAdd Pig Latin to the text (PIGLATIN)\nShift your text into Ceasar Cipher (CAESAR)\nWhich mode would you like to use? "))
    text_input = str(input("Input the string you need to convert here: "))
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

    elif mode.lower() == "EXIT":
        break

    else:
        print("Couldn't understand you. Did you perhaps misspell the mode?")
