import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library.TextConverter import TextConverter
import pyperclip

def main():
    parser = argparse.ArgumentParser(description="Text Converter")
    parser.add_argument("--mode", required=True, help="Conversion mode")
    parser.add_argument("text", nargs="+", help="Text to convert")
    parser.add_argument("--shift", type=int, default=3, help="Shift for Caesar cipher")
    parser.add_argument("--case", choices=['upper', 'lower'], default='upper', help="Case for case_switch")
    parser.add_argument("--save", action="store_true", help="Save the result to history file")
    parser.add_argument("--copy", action="store_true", help="Copy the result to clipboard")
    parser.add_argument("--filename", default="qr_code", help="Filename for QR code")

    args = parser.parse_args()

    converter = TextConverter()
    text = " ".join(args.text)

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
        "binary": converter.binary_text,
        "shadow": converter.text_shadow,
        "emoticons": converter.text_to_emoticons,
        "nerd": converter.nerd_mode,
        "scroll": converter.scroll_text,
        "qr": lambda t: converter.qr_code(t, args.filename)
    }

    if args.mode in mode_map:
        result = mode_map[args.mode](text)
        if isinstance(result, dict):
            output = "\n".join(f"{key}: {value}" for key, value in result.items())
        else:
            output = str(result)
        
        print(output)
        
        # Optionally save the result
        if args.save:
            converter.save_result(output, args.mode)
            print(f"Result saved to {converter.history_files[args.mode]}")
        
        # Copy result to clipboard if --copy flag is used and mode is not 'qr'
        if args.copy and args.mode != 'qr':
            pyperclip.copy(output)
            print("Result copied to clipboard")
    else:
        print(f"Unknown mode: {args.mode}")

if __name__ == "__main__":
    main()