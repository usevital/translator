import pyperclip
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library.TextConverter import TextConverter


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    print("\nText Converter Menu:")
    print("1. Reverse text")
    print("2. Flip characters")
    print("3. Both of the above")
    print("4. Enchant text")
    print("5. Change case")
    print("6. Convert to leetspeak")
    print("7. Scramble text")
    print("8. Convert to Pig Latin")
    print("9. Caesar cipher")
    print("10. ASCII art")
    print("11. Border text")
    print("12. Zalgo text")
    print("13. Morse code")
    print("14. Binary text")
    print("15. Shadow text")
    print("16. Scroll text")
    print("17. Generate QR code or barcode")
    print("18. Text to emoticons")
    print("19. Nerd mode")
    print("20. Convert to Braille")
    print("21. Convert to Pigpen")
    print("0. Exit")


def copy_to_clipboard(text):
    pyperclip.copy(text)
    print("Result copied to clipboard!")


def main():
    converter = TextConverter()

    while True:
        print_menu()
        choice = str(input("Enter your choice (0-20): "))

        if choice == '0':
            print("Thank you for using Text Converter. Goodbye!")
            break

        text = input("Enter the text to convert: ")
        result = None
        mode = None

        if choice == '1':
            result = converter.reverse_text(text)
            mode = 'reverse'
        elif choice == '2':
            result = converter.character_flip(text)
            mode = 'character_flip'
        elif choice ==  '3':
        elif choice == '4':
            result = converter.enchant_text(text)
            mode = 'enchant'
        elif choice == '5':
            case = input("Enter 'upper' or 'lower': ")
            result = converter.case_switch(text, case)
            mode = 'case'
        elif choice == '6':
            result = converter.leetspeak(text)
            mode = 'leetspeak'
        elif choice == '7':
            result = converter.scramble_text(text)
            mode = 'scramble'
        elif choice == '8':
            result = converter.piglatin(text)
            mode = 'piglatin'
        elif choice == '9':
            shift = int(input("Enter the shift value: "))
            result = converter.caesar_cipher(text, shift)
            mode = 'caesar'
        elif choice == '10':
            result = converter.ascii_art(text)
            mode = 'ascii'
        elif choice == '11':
            result = converter.border_text(text)
            mode = 'border'
        elif choice == '12':
            result = converter.zalgo_text(text)
            mode = 'zalgo'
        elif choice == '13':
            result = converter.morse_code(text)
            mode = 'morse'
            print(result)
            play_sound = input("Do you want to generate and play the Morse code sound? (y/n): ").lower()
            if play_sound == 'y':
                mode = 'morse_sound'
                audio_result = converter.morse_code_audio(text)
                print(f"Audio file generated: {audio_result}")
                save_audio = input("Do you want to keep the audio file? (y/n): ").lower()
                if save_audio == 'y':
                    print(f"Audio file saved as {audio_result}")
                    input("\nPress any key to continue...")
                    clear_screen()
                    continue
                else:
                    os.remove(audio_result)
                    print("Audio file deleted.")
                    input("\nPress any key to continue...")
                    clear_screen()
                    continue
        elif choice == '14':
            result = converter.binary_text(text)
            mode = 'binary'
        elif choice == '15':
            result = converter.text_shadow(text)
            mode = 'shadow'
        elif choice == '16':
            converter.scroll_text(text)
            input("\nPress any key to continue...")
            clear_screen()
            continue
        elif choice == '17':
            code_type = input("Enter 'qr' for QR code or 'barcode' for barcode: ")
            filename = input("Enter the filename for the code: ")
            result = converter.generate_code(text, code_type, filename)
            mode = 'qr' if code_type == 'qr' else 'barcode'
        elif choice == '18':
            result = converter.text_to_emoticons(text)
            mode = 'emoticons'
        elif choice == '19':
            result = converter.nerd_mode(text)
            mode = 'nerd'
        elif choice == '20':
            result = converter.text_to_braille(text)
            mode = 'braille'
        elif choice == '21':
            result = converter.pigpen_mode(text)
            mode = 'pigpen'
        else:
            print("Invalid choice. Please try again.")
            continue

        if isinstance(result, dict):
            for key, value in result.items():
                print(f"{key}: {value}")
        elif result:
            print(result)

        if mode not in ['qr', 'barcode', 'morse_sound']:
            copy_choice = input("Do you want to copy the result to clipboard? (y/n): ").lower()
            if copy_choice == 'y':
                if isinstance(result, dict):
                    copy_to_clipboard(str(result))
                else:
                    copy_to_clipboard(result)

            save_choice = input("Do you want to save the result to a history file? (y/n): ").lower()
            if save_choice == 'y':
                save_message = converter.save_result(result, mode)
                print(save_message)

        input("\nPress any key to continue...")
        clear_screen()


if __name__ == "__main__":
    main()
