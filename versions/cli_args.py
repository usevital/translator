import argparse
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from library.TextConverter import TextConverter


def main():
    parser = argparse.ArgumentParser(description="Text Converter")
    parser.add_argument("--mode", required=True, help="Conversion mode")
    parser.add_argument("text", nargs="+", help="Text to convert")
    parser.add_argument("--shift", type=int, default=3, help="Shift for Caesar cipher")
    parser.add_argument("--case", choices=['upper', 'lower'], default='upper', help="Case for case_switch")
    parser.add_argument("--filename", default="qr_code", help="Filename for QR code")
    parser.add_argument("--save", action="store_true", help="Save the result to history file")

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
        "qr": lambda t: converter.qr_code(t, args.filename),
        "scroll": converter.scroll_text
    }

    if args.mode in mode_map:
        result = mode_map[args.mode](text)
        if isinstance(result, dict):
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print(result)
        
        # Optionally save the result
        if args.save:
            converter.save_result(result, args.mode)
            print(f"Result saved to {converter.history_files[args.mode]}")
    else:
        print(f"Unknown mode: {args.mode}")

if __name__ == "__main__":
    main()