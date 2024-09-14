import argparse
import sys
import os
import pyperclip
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library.TextConverter import TextConverter


def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Unable to read file '{file_path}'.")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Text Converter")
    parser.add_argument("--mode", required=True, help="Conversion mode")
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("text", nargs="?", help="Text to convert (in quotes)")
    input_group.add_argument("--file", help="Path to input file")
    parser.add_argument("--shift", type=int, default=3, help="Shift for Caesar cipher")
    parser.add_argument("--case", choices=['upper', 'lower'], default='upper', help="Case for case_switch")
    parser.add_argument("--save", action="store_true", help="Save the result to history file")
    parser.add_argument("--copy", action="store_true", help="Copy the result to clipboard")
    parser.add_argument("--filename", help="Filename for QR code or barcode")

    args = parser.parse_args()

    converter = TextConverter()

    if args.file:
        text = read_file(args.file)
    elif args.text:
        text = args.text
    else:
        parser.error("Either 'text' or '--file' must be provided.")

    mode_map = {
        "reverse": converter.reverse_text,
        "flip": converter.text_flip,
        "enchant": converter.enchant_text,
        "case": lambda t: converter.case_switch(t, args.case),
        "leetspeak": converter.leetspeak,
        "scramble": converter.scramble_text,
        "piglatin": converter.piglatin,
        "caesar": lambda t: converter.caesar_cipher(t, args.shift),
        "ascii": converter.ascii_art,
        "border": converter.border_text,
        "zalgo": converter.zalgo_text,
        "morse": converter.morse_code,
        "morse_sound": converter.morse_code_audio,
        "binary": converter.binary_text,
        "shadow": converter.text_shadow,
        "emoticons": converter.text_to_emoticons,
        "nerd": converter.nerd_mode,
        "scroll": converter.scroll_text,
        "qr": lambda t: converter.generate_code(t, 'qr', args.filename),
        "barcode": lambda t: converter.generate_code(t, 'barcode', args.filename),
        "braille": converter.text_to_braille,
        "pigpen": converter.pigpen_mode
    }

    if args.mode in mode_map:
        result = mode_map[args.mode](text)

        if args.mode == "morse_sound":
            print("Morse code audio played.")
            save_audio = input("Do you want to keep the audio file? (y/n): ").lower().strip()
            if save_audio == 'y':
                print(f"Audio saved as {result}")
            else:
                os.remove(result)
                print("Audio file deleted.")
        elif isinstance(result, dict):
            output = "\n".join(f"{key}: {value}" for key, value in result.items())
            print(output)
        else:
            print(result)
   
        # Optionally save the result
        if args.save and args.mode not in ["morse_sound", "qr", "barcode"]:
            converter.save_result(result, args.mode)
            print(f"Result saved to {converter.history_files[args.mode]}")

        # Copy result to clipboard if --copy flag is used and mode is not 'qr', 'barcode', or 'morse_sound'
        if args.copy and args.mode not in ['qr', 'barcode', 'morse_sound']:
            pyperclip.copy(str(result))
            print("Result copied to clipboard")
    else:
        print(f"Unknown mode: {args.mode}")


if __name__ == "__main__":
    main()
