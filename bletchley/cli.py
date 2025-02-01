"""
Client facing file to interface with Bletchley tools

TODO:
"""

from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread
import itertools
import argparse
import warnings

from . import start
from . import recognizeHash
from . import frequency
from . import encodings
from . import ciphers
from bletchley import __version__

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
    start.run(text, wordlist, verbose)

def encrypt_caesar(text, key):
    print(ciphers.caesar.encrypt(text, key))

def decrypt_caesar(text, key):
    print(ciphers.caesar.decrypt(text, key))

def about_caesar():
    print(ciphers.caesar.about(False)) # Using the standard/default Caesar cipher about section

def encrypt_playfair(text, key):
    print(ciphers.playfair.encrypt(text, ciphers.playfair.generate_key_matrix(key)))

def decrypt_playfair(text, key):
    print(ciphers.playfair.decrypt(text, ciphers.playfair.generate_key_matrix(key)))

def about_playfair():
    print(ciphers.playfair.about())

def encrypt_multiplication(text, key):
    print(ciphers.multiplication.encrypt(text, key))

def decrypt_multiplication(text, key):
    print(ciphers.multiplication.decrypt(text, key))

def encrypt_rot13(text):
    print(ciphers.caesar.encrypt(text, 13))

def decrypt_rot13(text):
    print(ciphers.caesar.decrypt(text, 13))

def about_rot13():
    print(ciphers.caesar.about(True)) # Using an alternative Caesar cipher about section (for ROT13)

def encrypt_vigenere(text, password):
    print(ciphers.vigenere.encrypt(text, password))

def decrypt_vigenere(text, password):
    print(ciphers.vigenere.decrypt(text, password))

def about_vigenere():
    print(ciphers.vigenere.about())

def atbash(text):
    print(ciphers.atbash.atbash(text))

# TODO: about_atbash()

# SKIPPING BACONIAN FOR NOW TO AVOID CONFLICT
def encrypt_baconian(text, style, letter1="a", letter2="b"):
    print(ciphers.baconian(text, "e", letter1, letter2, style))

def decrypt_baconian(text, style, letter1="a", letter2="b"):
    print(ciphers.baconian(text, "d", letter1, letter2, style))

def encrypt_affine(text, p1, p2):
    print(ciphers.affine(text, p1, p2, "e"))

def decrypt_affine(text, p1, p2):
    print(ciphers.affine(text, p1, p2, "d"))

def about_affine():
    print(ciphers.affine.about())

def encrypt_rail_fence(text, key):
    print(ciphers.rail_fence(text, key, "e"))

def decrypt_rail_fence(text, key):
    print(ciphers.rail_fence(text, key, "d"))

def about_rail_fence():
    print(ciphers.rail_fence.about())

def encrypt_substitution(text, key):
    print(ciphers.substitution.encrypt(text, key))

def decrypt_substitution(text, key):
    print(ciphers.substitution.decrypt(text, key))

def about_substitution():
    print(ciphers.substitution.about())

def encrypt_beaufort(text, key):
    print(ciphers.beaufort.beaufort(text, key))

def decrypt_beaufort(text, key):
    print(ciphers.beaufort.beaufort(text, key))

def about_beaufort():
    print(ciphers.beaufort.about())

def encrypt_autokey(text, key):
    print(ciphers.autokey.encrypt(text, key))

def decrypt_autokey(text, key):
    print(ciphers.autokey.decrypt(text, key))

def about_autokey():
    print(ciphers.autokey.about())

def encrypt_bifid(text, key):
    print(ciphers.encrypt_bifid(text, key))

def decrypt_bifid(text, key):
    print(ciphers.decrypt_bifid(text, key))

def about_bifid():
    print(ciphers.bifid.about())


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
    
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')   

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
    run_parser.add_argument("-w", "--wordlist", choices=["large", "small", "small_specialized", "large_specialized", "dictionary"], type=str, required=False, help="The word list to use when detecting whether a tested ciphertext is decrypted or not")

    encryption_parser = subparsers.add_parser("encrypt", help="Encrypt a text.")
    encryption_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    encryption_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to encrypt the text with")
    encryption_parser.add_argument("-p", "--password", type=str, required=False, help="The password to encrypt the text with")

    decryption_parser = subparsers.add_parser("decrypt", help="Decrypt a text.")
    decryption_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    decryption_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to decrypt the text with")
    decryption_parser.add_argument("-p", "--password", type=str, required=False, help="The password to decrypt the text with")

    about_parser = subparsers.add_parser("about", help="Get more information about a cipher.")
    about_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to get information about")

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

        if args.cipher == "multiplicative" or args.cipher == "14" or args.cipher == "multiplication":
            check_text_password(args.text, args.password)
            encrypt_multiplication(args.text, int(args.password))

        elif args.cipher == "vigenere" or args.cipher == "2":
            check_text_password(args.text, args.password)
            encrypt_vigenere(args.text, args.password)

        elif args.cipher == "rot13" or args.cipher == "rot" or args.cipher == "3":
            check_password_not_needed(args.password)
            encrypt_rot13(args.text)

        elif args.cipher == "atbash" or args.cipher == "4":
            check_password_not_needed(args.password)
            atbash(args.text)

        elif args.cipher == "playfair" or args.cipher == "5":
            check_text_password(args.text, args.password)
            encrypt_playfair(args.text, args.password)

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

        else: # MUST BE LAST IN CHAIN
            print("Please select a valid cipher (e.g. '-c caesar').")

    elif args.command == "decrypt" or args.command == "de" or args.command == "d":
        if args.cipher == "caesar" or args.cipher == "1":
            check_text_password(args.text, args.password)
            decrypt_caesar(args.text, int(args.password))

        if args.cipher == "multiplicative" or args.cipher == "14" or args.cipher == "multiplication":
            check_text_password(args.text, args.password)
            decrypt_multiplication(args.text, int(args.password))

        elif args.cipher == "vigenere" or args.cipher == "2":
            check_text_password(args.text, args.password)
            decrypt_vigenere(args.text, args.password)

        elif args.cipher == "rot13" or args.cipher == "rot" or args.cipher == "3":
            check_password_not_needed(args.password)
            decrypt_rot13(args.text)

        elif args.cipher == "atbash" or args.cipher == "4":
            check_password_not_needed(args.password)
            atbash(args.text)

        elif args.cipher == "playfair" or args.cipher == "5":
            check_text_password(args.text, args.password)
            decrypt_playfair(args.text, args.password)

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

        else:
            print("Please select a valid cipher (e.g. '-c caesar').")

    elif args.command == "about" or args.command == "info":
        if args.cipher == "caesar" or args.cipher == "1":
            about_caesar()

        elif args.cipher == "vigenere" or args.cipher == "2":
            about_vigenere()
        
        elif args.cipher == "rot13" or args.cipher == "rot" or args.cipher == "3":
            about_rot13()

        # elif args.cipher == "atbash" or args.cipher == "4":
        #     about_atbash()

        elif args.cipher == "playfair" or args.cipher == "5":
            about_playfair()

        # elif args.cipher == "baconian" or args.cipher == "6":
        #     about_baconian

        elif args.cipher == "affine" or args.cipher == "7":
            about_affine()

        elif args.cipher == "rail" or args.cipher == "rail_fence" or args.cipher == "8":
            about_rail_fence()

        elif args.cipher == "substitution" or args.cipher == "9":
            about_substitution()

        elif args.cipher == "beaufort" or args.cipher == "10":
            about_beaufort()

        elif args.cipher == "autokey" or args.cipher == "11":
            about_autokey()

        elif args.cipher == "bifid" or args.cipher == "12":
            about_bifid()

        else:
            print("Please select a valid cipher (e.g. '-c caesar').")

    elif args.command == "measure" or args.command == "m":
        print("Measure things like ioc, bigrams and trigrams")

    else:
        help()


if __name__ == "__main__":
    main()
