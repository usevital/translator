# Features

To use these as args in CLI, input `--mode` then the arg in [square brackets] next to the feature you want to use. You can also input `-h` in the CLI to get a list of all the features.

The string you want to convert should in inputted with quotation marks around them.

Example: `--mode case --case lower "Hello World!"`

- Forces characters into all UPPERCASE/lowercase [case --case [upper|lower]]
- Flips text uʍop ǝpᴉsdn. [flip]
- Translations to the Standard Galactic Alphabet aka Minecraft enchanting table language (by @Thinkseal) [enchant]
- Convert to l33tsp34k [leetspeak]
- ctxbetm lraSe (Scramble text) [scramble]
- Convert to Pig Latin (ello world!Hay) [piglatin]
- Convert to 7h1r1f1c470r14n (Caesar cipher) [casesar --shift [int:shift_level]]
- Convert to ASCII art [ascii]
- Add borders to text via ASCII [border]
- Add ͫŽa̋l̓g͑o to your text [zalgo]
- Convert to -- --- .-. ... .  -.-. --- -.. . (Morse code) [morse]

  To play the Morse code audibly, use `morse_sound` instead.

- Convert to 01000010 01101001 01101110 01100001 01110010 01111001 (Binary) [binary]
- Add text shadows [shadow]
- Convert ➡️ Emoticons [emoticon]
- Convert to [QR codes](./images/qr-code.png) [qr --filename [str:name]]
- Generate barcodes [barcode --filename [str:name]]
- Counts your words, characters, and more :nerd_face: [nerd]
- Convert to Braille [braille]
- Convert to Pigpen cipher [pigpen]
- Scroll text (terminal GUI only) [scroll]

...and more coming soon (maybe)!

The scripts also allow you to do the following:

- Read input from a file instead of command line [--file [path_to_file]]
  Example: `python versions/cli_args.py --mode reverse --file hello.txt --save`

- Save the result into conversion-history/{mode}_history.txt [--save]
  
  For QR codes and barcodes, they are _always_ saved inside conversion-history/qr_codes/ and conversion-history/barcodes/ respectively.
  
  For Morse code audio, the MP3 file is saved in conversion-history/ and you'll be asked if you want to keep it after playing.
  
- Copy the result to clipboard (not supported by QR code, barcode, or Morse sound modes) [--copy]

Note: When using --file, the --text argument should not be used. The content of the file will be used as input for the conversion.
