import logging 

logging.basicConfig(filename='output.txt', level=logging.INFO, format='')

i = 0

print("At any time, type EXIT to stop. ")
while i < 1:
    mode = int(input("Type 1 for uppercase, 2 for lowercase. "))
    text_input = str(input("What would you like to fully uppercase/lowercase? "))

    if mode == 1:
        converted_text = text_input.upper()
        print("The result is: ", converted_text)
        with open('output.txt', 'a') as f:
            f.write('\n')
            f.write(converted_text)
        print("I also added the converted text into a file called output.txt, if it's easier to copy from there.")
        redo = str(input("Continue? (y/n) "))
        if redo == "y":
            i += 1
        elif redo == "n":
            break
    elif mode == 2:
        converted_text = text_input.lower()
        print("The result is: ", converted_text)
        with open('output.txt', 'a') as f:
            f.write('\n')
            f.write(converted_text)
        print("I also added the converted text into a file called output.txt, if it's easier to copy from there.")
        redo = str(input("Continue? (y/n) "))
        if redo == "y":
            i += 1
        elif redo == "n":
            break