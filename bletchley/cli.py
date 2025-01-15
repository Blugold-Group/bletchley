#!/usr/bin/venv python
"""
Client facing file to interface with Bletchley tools

"""

from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread
import itertools

#from bletchley import __version__
import argparse
import start
import recognizeHash
import frequency
import encodings
import ciphers
import warnings

def frequencyAnalysis(text, style="vbcol"):
    if style=="p" or style=="c":
        print(frequency.frequencyAnalysis(text, style))
    else:
        frequency.frequencyAnalysis(text, style)

def hash(text):
    recognizeHash.guess(text)

def bruteForce(text, cipher):
    print("Brute force", text, cipher)

def auto_decode(text):
    # Decode without knowing the encoding
    encoding.bruteforce(text)

def encode(text, encoding):
    # Encode the text
    encoding.encode(text, encoding)

def decode(text, encoding):
    # Decode the text according to a given encoding
    print("Decode")
    encoding.decode(text, encoding)

def classify(text):
    print("Using ML classification to find cipher")

def run(text, wordlist="small_specialized", verbose=False):
    print(start.run(text, wordlist, verbose))

def encrypt_caesar(text, key):
    print(ciphers.caesar(text, key))

def decrypt_caesar(text, key):
    print(ciphers.caesar(text, 26-key))

def encrypt_rot13(text):
    print(ciphers.rot13(text, "e"))

def decrypt_rot13(text):
    print(ciphers.rot13(text, "d"))

def encrypt_vigenere(text, password):
    print(ciphers.vigenere(text, password, "e"))

def decrypt_vigenere(text, password):
    print(ciphers.vigenere(text, password, "d"))

def atbash(text):
    print(ciphers.atbash(text))

def encrypt_baconian(text, style, letter1="a", letter2="b"):
    print(ciphers.baconian(text, "e", letter1, letter2, style))

def decrypt_baconian(text, style, letter1="a", letter2="b"):
    print(ciphers.baconian(text, "d", letter1, letter2, style))

def encrypt_affine(text, p1, p2):
    print(ciphers.affine(text, p1, p2, "e"))

def decrypt_affine(text, p1, p2):
    print(ciphers.affine(text, p1, p2, "d"))

def encrypt_rail_fence(text, key):
    print(ciphers.rail_fence(text, key, "e"))

def decrypt_rail_fence(text, key):
    print(ciphers.rail_fence(text, key, "d"))

def encrypt_substitution(text, key):
    print(ciphers.substitution_encrypt(text, key))

def decrypt_substitution(text, key):
    print(ciphers.substitution_decrypt(text, key))

def encrypt_beaufort(text, key):
    print(ciphers.beaufort(text, key))

def decrypt_beaufort(text, key):
    print(ciphers.beaufort(text, key))

def encrypt_autokey(text, key):
    print(ciphers.autokey_encrypt(text, key))

def decrypt_autokey(text, key):
    print(ciphers.autokey_decrypt(text, key))

def encrypt_bifid(text, key):
    print(ciphers.encrypt_bifid(text, key))

def decrypt_bifid(text, key):
    print(ciphers.decrypt_bifid(text, key))


def check_text_password(text, password):
    if text is None:
        raise Exception("You need to pass a text to encrypt with `-t <plaintext>`")
    if password is None:
        raise Exception("This cipher requires a password, tell bletchley which password to use with `-p <password>`")

def check_password_not_needed(password):
    if password is not None:
        warnings.warn("This cipher doesn't require a password", SyntaxWarning)

def convert_num_password(password):
    try:
        return(int(password))
    except:
        raise Exception("Key for this cipher must be an integer")

def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="CLI for Bletchley, a cryptanalysis suite.")    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    #parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')
    
    frequency_parser = subparsers.add_parser("freq", help="Do frequency analysis.")
    frequency_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    frequency_parser.add_argument("-c", "--chart", choices=["c", "p", "vsbc", "vbc", "vsbca", "vbca", "vsbcar", "vbcar", "vcbcos", "vbcos", "vsbcol", "vbcol"], type=str, required=False, help="The style for the bar chart")
    
    brute_parser = subparsers.add_parser("force", help="Brute force the ciphertext knowing the cipher.")
    brute_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    brute_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to brute force")

    hash_parser = subparsers.add_parser("hash", help="Identify and reverse lookup a hash.")
    hash_parser.add_argument("-t", "--text", type=str, required=True, help="The hash to process")
    
    encoding_parser = subparsers.add_parser("decode", help="Decode a text, with or without the encoding.")
    encoding_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    encoding_parser.add_argument("-e", "--encoding", type=str, required=False, help="The encoding the text is in") # This is optional, if its not passed that means the encoding is unknown and should be found

    encoding_parser = subparsers.add_parser("encode", help="Find the encoding the text is in and/or encode the text.")
    encoding_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    encoding_parser.add_argument("-e", "--encoding", type=str, required=True, help="The encoding to encode the text with")

    learning_parser = subparsers.add_parser("classify", help="Use the machine learning model to detect which cipher was used to encrypt the text.")
    learning_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    
    run_parser = subparsers.add_parser("run", help="Try to automatically decrypt the ciphertext.")
    run_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    run_parser.add_argument("-v", "--verbose", action="store_true", help="Print the results of all tests")
    run_parser.add_argument("-w", "--wordlist", type=str, required=False, help="The word list to use when detecting whether a tested ciphertext is decrypted or not")

    encryption_parser = subparsers.add_parser("encrypt", help="Encrypt a text.")
    encryption_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    encryption_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to encrypt the text with")
    encryption_parser.add_argument("-p", "--password", type=str, required=False, help="The password to encrypt the text with")

    decryption_parser = subparsers.add_parser("decrypt", help="Decrypt a text.")
    decryption_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    decryption_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to decrypt the text with")
    decryption_parser.add_argument("-p", "--password", type=str, required=False, help="The password to decrypt the text with")

    # Parse the arguments
    args = parser.parse_args()

    # Handle the commands
    if args.command == "freq":
        if args.chart is not None:
            frequencyAnalysis(args.text, args.chart)
        else:
            frequencyAnalysis(args.text)
    
    elif args.command == "force":
        bruteForce(args.text, args.cipher) # This will run for a while depending on how long, it should run a loading icon while working
    
    elif args.command == "hash":
        hash(args.text)

    elif args.command == "decode":
        if args.encoding is not None:
            decode(args.text, args.encoding)
        else:
            auto_decode(args.text)

    elif args.command == "encode":
        encode(args.text, args.encoding)

    elif args.command == "run":
        if args.verbose and args.wordlist is not None:
            run(args.text, args.wordlist, True)
        elif args.verbose:
            run(args.text, "small_specialized", True)
        elif args.wordlist is not None:
            run(args.text, args.wordlist)
        else:
            run(args.text)

    elif args.command == "encrypt" or args.command == "en" or args.command == "e":
        if args.cipher == "caesar" or args.cipher == "1":
            check_text_password(args.text, args.password)
            encrypt_caesar(args.text, int(args.password))

        elif args.cipher == "vigenere" or args.cipher == "2":
            check_text_password(args.text, args.password)
            encrypt_vigenere(args.text, args.password)

        elif args.cipher == "rot13" or args.cipher == "3":
            check_password_not_needed(args.password)
            encrypt_rot13(args.text)

        elif args.cipher == "atbash" or args.cipher == "4":
            check_password_not_needed(args.password)
            atbash(args.text)

        elif args.cipher == "playfair" or args.cipher == "5":
            check_text_password(args.text, args.password)

            print("The Playfair cipher has not been added yet")

        elif args.cipher == "baconian" or args.cipher == "6":
            print("I need to get the optional letter 1 and 2, and style (old or new), I could probably do this with the -p, just have them passed with commas in that")

        elif args.cipher == "affine" or args.cipher == "7":
            check_text_password(args.text, args.password)
            print("Decryption apparently doesn't work for this")

            if args.password.count(',') < 1:
                raise Exception("The affine cipher needs two number keys, pass them with `-p num1,num2` (with a comma)")

        elif args.cipher == "rail" or args.cipher == "rail_fence" or args.cipher == "8":
            encrypt_rail_fence(args.text, convert_num_password(args.password))

        elif args.cipher == "substitution" or args.cipher == "9":
            encrypt_substitution(args.text, args.password)

        elif args.cipher == "beaufort" or args.cipher == "10":
            encrypt_beaufort(args.text, args.password)

        elif args.cipher == "autokey" or args.cipher == "11":
            encrypt_autokey(args.text, args.password)

        elif args.cipher == "bifid" or args.cipher == "12":
            encrypt_bifid(args.text, args.password)

    elif args.command == "decrypt" or args.command == "de" or args.command == "d":
        if args.cipher == "caesar" or args.cipher == "1":
            check_text_password(args.text, args.password)
            decrypt_caesar(args.text, int(args.password))

        elif args.cipher == "vigenere" or args.cipher == "2":
            check_text_password(args.text, args.password)
            decrypt_vigenere(args.text, args.password)

        elif args.cipher == "rot13" or args.cipher == "3":
            check_password_not_needed(args.password)
            decrypt_rot13(args.text)

        elif args.cipher == "atbash" or args.cipher == "4":
            check_password_not_needed(args.password)
            atbash(args.text)

        elif args.cipher == "playfair" or args.cipher == "5":
            check_text_password(args.text, args.password)

            print("The Playfair cipher has not been added yet")

        elif args.cipher == "baconian" or args.cipher == "6":
            print("I need to get the optional letter 1 and 2, and style (old or new), I could probably do this with the -p, just have them passed with commas in that")

        elif args.cipher == "affine" or args.cipher == "7":
            check_text_password(args.text, args.password)
            print("Decryption apparently doesn't work for this")

            if args.password.count(',') < 1:
                raise Exception("The affine cipher needs two number keys, pass them with `-p num1,num2` (with a comma)")

        elif args.cipher == "rail" or args.cipher == "rail_fence" or args.cipher == "8":
            decrypt_rail_fence(args.text, convert_num_password(args.password))

        elif args.cipher == "substitution" or args.cipher == "9":
            decrypt_substitution(args.text, args.password)

        elif args.cipher == "beaufort" or args.cipher == "10":
            decrypt_beaufort(args.text, args.password)

        elif args.cipher == "autokey" or args.cipher == "11":
            decrypt_autokey(args.text, args.password)

        elif args.cipher == "bifid" or args.cipher == "12":
            decrypt_bifid(args.text, args.password)

    elif args.command == "measure" or args.command == "m":
        print("Measure things like ioc, bigrams and trigrams")

    else:
        help()


if __name__ == "__main__":
    main()
