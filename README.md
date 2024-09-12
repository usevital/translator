# translator

![Made in Python badge](./images/made-in-python.svg)

Originally called `text-conversions` and then called `text-manipulations`, this script can help you convert and manipulate your text into many different ways! (hence the names)

This script was originally made for [NotEssential](https://notessential.blurry.gay) by @KTrain5169

## Features

To use these as args in CLI, input `--mode` then the arg in [square brackets] next to the feature you want to use.

Example: `--mode case --case lower <string>`

- Forces characters into all UPPERCASE/lowercase [case --case [upper|lower]]
- Flips text uʍop ǝpᴉsdn. [flip]
- Translations to the Standard Galactic Alphabet aka Minecraft enchanting table language (by @Thinkseal) [enchant]
- Convert to l33tsp34k [leetspeak]
- ctxbetm lraSe (Scramble text) [scramble]
- Convert to Pig Latin (ello world!Hay) [piglatin]
- Convert to 7h1r1f1c470r14n (Caesar cipher) [casesar --shift [int:shift_level]]
- Convert to ASCII art [ascii]
- Add borders to text via ASCII [border]
- Add ͫŽa̋l̓g͑o to your text [zalgo]
- Convert to -- --- .-. ... .  -.-. --- -.. . (Morse code) [morse]
- Convert to 01000010 01101001 01101110 01100001 01110010 01111001 (Binary) [binary]
- Add text shadows [shadow]
- Convert ➡️ Emoticons [emoticon]
- Convert to [QR codes](./images/qr-code.png) [qr --filename [str:name]]
- Counts your words, characters, and more :nerd_face: [nerd]

...and more coming soon (maybe)!

The scripts also do allow you to do the following (CLI users can append these args to the above):
* Save the result into conversion-history/{mode}_history.txt [--save]
  
  For QR codes, they are _always_ saved inside conversion-history/{--filename arg}.png
  
* Copy the result to clipboard (not supported by QR code mode) [--copy]

Want to try this project but don't want to download something? Try [Ward](https://ward.worldwidepixel.ca), the web-based version of this project made by @worldwidepixel!

## Installation

You may either download a release from the [releases page](https://github.com/notessentialsite/translator/releases) or install the dependencies and run the source code.

### How to run the source code

```bash
git clone https://github.com/notessentialsite/translator.git
cd translator
pip install -r requirements.txt
```
If you wish to use the terminal GUI version:
```bash
python versions/terminal_gui.py
```
If you want to use the CLI to pass arguments:
```bash
python versions/cli_args.py [insert arguments here]
```
If you choose to use the library file we included, that's cool by us, as long as you link back to this GitHub repository in your credits.
