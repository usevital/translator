import pyperclip

i = 0

def flipUD(text):
    flip_map = str.maketrans(
        "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890.,!?\"'()[]{}",
        "ɐqɔpǝɟƃɥᴉſʞʅɯuodbɹsʇnʌʍxʎz∀𐐒ƆᗡƎℲ⅁HIſʞ⅃WNOԀΌᴚS⊥∩ΛM⅄Z⇂ᘕԐત૨୧⌋8მ0˙ˋ¡¿\„,)(][}{"
    )

    return text.translate(flip_map)[::-1]
def enchant_text(text):
    enchanted_text = str.maketrans(
        "abcdefghijklmnoqrstuvwzABCDEFGHIJKLMNOQRSTUVWZ1234567890.,!?\"'()[]{}",
        "ᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹ᑑ∷ᓭℸ⚍⍊∴Λᔑʖᓵ↸ᒷ⎓⊣⍑╎⋮ꖌꖎᒲリ𝙹ᑑ∷ᓭℸ⚍⍊∴Λ1234567890.,!?\"'()[]{}"
    )
    enchanted_text = str(enchanted_text).replace('p', '!¡').replace('P', '!¡').replace('y', '||').replace('Y', '||').replace('x', '/̇').replace('X', '/̇')
    print("The result is: ", enchanted_text)
    pyperclip.copy(enchanted_text)
    with open('flip_history.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(enchanted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called output.txt (if you made one called that in this directory), if it's easier to copy from there.")    

def text_flip(flip_this):
    converted_text = flipUD(flip_this)
    print("The result is: ", converted_text)
    pyperclip.copy(converted_text)
    with open('flip_history.txt', 'a', encoding="utf-8") as f:
        f.write('\n')
        f.write(converted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called output.txt (if you made one called that in this directory), if it's easier to copy from there.")

def case_switch(case, text):
    if case == 1:
        converted_text = text.upper()
    elif case == 2:
        converted_text = text.lower()
    else:
        print("Something went wrong.")
    print(f"The result is: {converted_text}")
    pyperclip.copy(converted_text)
    with open('case_history.txt', 'a') as f:
        f.write('\n')
        f.write(converted_text)
    print("For convenience, I've placed the converted text into your keyboard.")
    print("I also added it into a file called output.txt, if it's easier to copy from there.")

def prompt_redo():
    redo = str(input("Continue? (y/n) "))
    if redo == "y":
        return "redo"
    elif redo == "n":
        return "stop"


print("At any time, type EXIT to stop. ")
while i < 1:
    mode = str(input("What mode do you wish to use? FLIP == flip text, CASE == change casing ENCHANT == Convert text to the standard galactic alphabet used by the Minecraft enchanting table "))
    text_input = str(input("Input the string you need to convert here: "))
    if mode.lower() == "case":
        casing = int(input("Type 1 for uppercase, 2 for lowercase. "))
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

    elif mode.lower() == "EXIT":
        i = 1
    else:
        print("Couldn't understand you. Did you perhaps misspell the mode?")
