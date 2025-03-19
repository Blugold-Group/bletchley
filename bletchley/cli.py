"""
Client-facing CLI file for interfacing with Bletchley cryptanalysis tools.

This script provides command-line access to encryption, decryption,
hash recognition, frequency analysis, brute force decryption, and more.

Usage:
    bletchley <command> [options]

Commands:
    - freq: Perform frequency analysis on text.
    - hash: Identify and reverse lookup a hash.
    - encode: Encode text using various encoding formats.
    - decode: Decode text using various encdoing formats.
    - encrypt: Encrypt text using a specified cipher.
    - decrypt: Decrypt text using a specified cipher.
    - force: Attempt bruteforce decryption on a ciphertext.
    - classify: Use our machine learning model to classify a cipher.
    - about: Display information about a cipher.
    - run: Automatically attempt to decrypt a ciphertext.

Authors:
    The Blugold Group
        - Jack Hagen
        - Jacob Stoltenburg
        - Silas Eacret
"""

from sys import stdout as terminal
import sys
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
from . import bruteforce
from bletchley import __version__


# ---- Frequency analysis

def frequencyAnalysis(text, style="vbcol"):
    """
    Performs frequency analysis on a given text.

    Args:
        text (str): The text to analyze.
        style (str, optional): The display stile for the frequency chart.
            Default is "vbcol" (vertical bar colored).

    Output:
        Prints a frequency analysis output or chart.
    """
    if style=="p" or style=="c":
        print(frequency.frequencyAnalysis(text, style))
    else:
        frequency.frequencyAnalysis(text, style)


# ---- Hashes

def hash(text):
    """
    Identifies a hash type and attempts reverse lookup.

    Args:
        text (str): The hash string to analyze.

    Output:
        The identified hash type and possible plaintext values.
    """
    recognizeHash.guess(text)


# ---- Automatic solving

def auto_decode(text):
    """
    Attempts to decode text by detecting the encoding automatically.

    Args:
        text (str): The encoded text.

    Output:
        Prints the decoded plaintext if successful.
    """
    encoding.bruteforce(text)

def run(text, wordlist="small_specialized", verbose=False):
    """
    Runs automatic cryptanalysis on the input text.

    Args:
        text (str): The text to analyze.
        wordlist (str, optional): The wordlist to use for decryption. Defaults to "small_specialized".
        verbose (bool, optional): Whether to print detailed output. Defaults to False.

    Output:
        Prints possible plaintext matches based on analysis.
    """
    start.run(text, wordlist, verbose)


# ---- Brute forcing

def force_caesar(text):
    """
    Attempts brute-force decryption on a Caesar cipher.

    Args:
        text (str): The ciphertext to decrypt.

    Output:
        Prints possible plaintext values with shift keys.
    """
    test = bruteforce.caesar(text)
    if (test):
        start.test_success(test[0], "caesar", test[1], test[2])
        return
    start.test_failed("Caesar Cipher", True)

def force_vigenere(text):
    """
    Attempts bruteforce decryption on a Vigenère cipher.

    Args:
        text (str): The ciphertext to decrypt.

    Output:
        Prints possible plaintext and key.
    """
    test = bruteforce.vigenere(text)
    if (test):
        start.test_success(test[0], "vigenere", test[1], test[2])
        return
    start.test_failed("Vigenere Cipher", True)

def force_atbash(text):
    """
    Attempts decryption of text using the Atbash cipher.

    Args:
        text (str): The ciphertext to decrypt.

    Output:
        Prints decrypted plaintext.
    """
    test = bruteforce.atbash(text)
    if (test):
        start.test_success(test[0], "atbash", test[1], test[2])
        return
    start.test_failed("Atbash Cipher", True)


# ---- Encodings

def encode(text, encoding):
    """
    Encodes a given text using a specified encoding.

    Args:
        text (str): The plaintext to encode.
        encoding (str): The encoding type (e.g. Base64, Hex).

    Output:
        Prints the encoded text.
    """
    encodings.encode(text, encoding)

def decode(text, encoding):
    """
    Decodes a given text using a specified encoding scheme.

    Args:
        text (str): The encoded text.
        encoding (str): The encoding type to use.

    Output:
        Decoded plaintext.
    """
    encodings.decode(text, encoding)


# ---- ML classification

def classify(text):
    """
    Attempts to use our machine learning model to classify the cipher.

    Args:
        text (str): The input ciphertext to classify.

    Output:
        Prints the possible cipher used to encrypt the ciphertext.
    """
    print("Using ML classification to find cipher")

# ---- Encryption

def encrypt_caesar(text, key):
    """
    Encrypts text using the Caesar cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (int): The key/offset to use in encryption.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.caesar.encrypt(text, key))

def encrypt_playfair(text, key):
    """
    Encrypts text using the Playfair cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (str): The keyword to encrypt the plaintext with.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.playfair.encrypt(text, ciphers.playfair.generate_key_matrix(key)))

def encrypt_multiplication(text, key):
    """
    Encrypts text using the Multiplication cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (int): The key to encrypt the plaintext with.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.multiplication.encrypt(text, key))

def encrypt_rot13(text):
    """
    Encrypts text using the ROT13 cipher.
    This is the same as encrypting the plaintext using Caesar with key of 13.

    Args:
        text (str): The plaintext to encrypt.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.caesar.encrypt(text, 13))

def encrypt_vigenere(text, password):
    """
    Encrypts text using the Vigenère cipher.

    Args:
        text (str): The plaintext to encrypt.
        password (str): The keyword to encrypt the plaintext with.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.vigenere.encrypt(text, password))

def atbash(text):
    """
    Encrypts text using the Atbash cipher.

    Args:
        text (str): The plaintext to encrypt.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.atbash.atbash(text))

# TODO: about_atbash()

def encrypt_baconian(text, letter1="a", letter2="b", style="old"):
    """
    Encrypts text using the Baconian cipher.

    Args:
        text (str): The plaintext to encrypt.
        letter1 (str, char, optional): The first letter to use in Baconian cipher's output.
        letter2 (str, char, optional): The second letter to use in Baconian cipher's output.
        style (str, optional): The style of Baconian cipher to use ('old' or 'new'. Defaults to old).

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.baconian.encrypt(text, letter1, letter2, style))

def encrypt_affine(text, p1, p2):
    """
    Encrypts text using the Affine cipher.

    Args:
        text (str): The plaintext to encrypt.
        p1 (int): The first key to be used with multiplication (coprime to 26).
        p2 (int): The second key to be used with addition.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.affine.encrypt(text, p1, p2))

def encrypt_rail_fence(text, key):
    """
    Encrypts text using the Rail Fence cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (int): The number of rails to be used in encryption.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.rail_fence.encrypt(text, key))

def encrypt_substitution(text, key):
    """
    Encrypts text using a Substitution cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (str, 26 chars): The custom alphabet to substitute with.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.substitution.encrypt(text, key))

def encrypt_beaufort(text, key):
    """
    Encrypts text using the Beaufort cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (str): The keyword to encrypt the plaintext with.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.beaufort.beaufort(text, key))

def encrypt_autokey(text, key):
    """
    Encrypts text using the Autokey cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (int): The initial key to encrypt the plaintext with.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.autokey.encrypt(text, key))

def encrypt_bifid(text, key):
    """
    Encrypts text using the Bifid cipher.

    Args:
        text (str): The plaintext to encrypt.
        key (str): The Polybius square to encrypt the text with.

    Output:
        Prints the encrypted ciphertext.
    """
    print(ciphers.bifid.encrypt(text, key))

def nonsense(length):
    """
    Encrypts text using the Nonsense cipher.

    Args:
        length (int): The length of desired nonsensical output.

    Output:
        Prints the nonsensical output.
    """
    print(ciphers.nonsense.nonsense(length))


# ---- Decryption

def decrypt_caesar(text, key):
    """
    Decrypts text using the Caesar cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (int): The key used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.caesar.decrypt(text, key))

def decrypt_playfair(text, key):
    """
    Decrypts text using the Caesar cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (list): The key matrix used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.playfair.decrypt(text, ciphers.playfair.generate_key_matrix(key)))

def decrypt_multiplication(text, key):
    """
    Decrypts text using the Multiplication cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (int): The key used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.multiplication.decrypt(text, key))

def decrypt_rot13(text):
    """
    Decrypts text using the ROT13 cipher.
    This is the same as decrypting a Caesar cipher with a shift key of 13.

    Args:
        text (str): The ciphertext to decrypt.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.caesar.decrypt(text, 13))

def decrypt_vigenere(text, password):
    """
    Decrypts text using the Vigenère cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (str): The keyword used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.vigenere.decrypt(text, password))

def decrypt_baconian(text, letter1="a", letter2="b", style="old"):
    print(ciphers.baconian.decrypt(text, letter1, letter2, style))

def decrypt_affine(text, p1, p2):
    """
    Decrypts text using the Affine cipher.

    Args:
        text (str): The ciphertext to decrypt.
        p1 (int): The first key used with multiplication (must be coprime to 26).
        p2 (int): The second key used with addition.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.affine.decrypt(text, p1, p2))

def decrypt_rail_fence(text, key):
    """
    Decrypts text using the Rail Fence cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (int): The number of rails used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.rail_fence.decrypt(text, key))

def decrypt_substitution(text, key):
    """
    Decrypts text using a Substitution cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (str, 26 characters): The custom alphabet used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.substitution.decrypt(text, key))

def decrypt_beaufort(text, key):
    """
    Decrypts text using the Beaufort cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (str): The keyword used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.beaufort.beaufort(text, key))

def decrypt_autokey(text, key):
    """
    Decrypts text using the Autokey cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (str): The initial keyword used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.autokey.decrypt(text, key))

def decrypt_bifid(text, key):
    """
    Decrypts text using the Bifid cipher.

    Args:
        text (str): The ciphertext to decrypt.
        key (str): The Polybius used to encrypt the plaintext.

    Output:
        Prints the decrypted plaintext.
    """
    print(ciphers.bifid.decrypt(text, key))


# ---- About ciphers

def about_caesar():
    """
    Provides information about the Caesar cipher.

    Output:
        Prints information about the Caesar cipher.
    """
    print(ciphers.caesar.about(False)) # Using the standard/default Caesar cipher about section

def about_playfair():
    """
    Provides information about the Playfair cipher.

    Output:
        Prints information about the Playfair cipher.
    """
    print(ciphers.playfair.about())

def about_rot13():
    """
    Provides information about the ROT13 cipher.

    Output:
        Prints information about the ROT13 cipher.
    """
    print(ciphers.caesar.about(True)) # Using an alternative Caesar cipher about section (for ROT13)

def about_vigenere():
    """
    Provides information about the Vigenère cipher.

    Output:
        Prints information about the Vigenère cipher.
    """
    print(ciphers.vigenere.about())

def about_affine():
    """
    Provides information about the Affine cipher.

    Output:
        Prints information about the Affine cipher.
    """
    print(ciphers.affine.about())

def about_rail_fence():
    """
    Provides information about the Rail Fence cipher.

    Output:
        Prints information about the Rail Fence cipher.
    """
    print(ciphers.rail_fence.about())

def about_substitution():
    """
    Provides information about the Substitution cipher.

    Output:
        Prints information about the Substitution cipher.
    """
    print(ciphers.substitution.about())

def about_beaufort():
    """
    Provides information about the Beaufort cipher.

    Output:
        Prints information about the Beaufort cipher.
    """
    print(ciphers.beaufort.about())

def about_autokey():
    """
    Provides information about the Autokey cipher.

    Output:
        Prints information about the Autokey cipher.
    """
    print(ciphers.autokey.about())

def about_bifid():
    """
    Provides information about the Bifid cipher.

    Output:
        Prints information about the Bifid cipher.
    """
    print(ciphers.bifid.about())

def about_nonsense():
    """
    Provides information about the Nonsense cipher.

    Output:
        Prints information about the Nonsense cipher.
    """
    print(ciphers.nonsense.about())


# ---- Utils

def check_text_password(text, password):
    """
    Checks whether input text and password/key have been provided.

    Raises:
        Exception: If input text has not been provided.
        Exception: If password/key has not been provided.
    """
    if text is None:
        raise Exception("You need to pass a text to encrypt with `-t <plaintext>`")
    if password is None:
        raise Exception("This cipher requires a password, tell bletchley which password to use with `-p <password>`")

def check_password_not_needed(password):
    """
    Runs if a user provides a password/key when attempting to use
    a cipher that does not require a password/key.

    Output:
        Prints a warning, notifying the user that the chosen cipher does not require a password.
    """
    if password is not None:
        warnings.warn("This cipher doesn't require a password", SyntaxWarning)

def convert_num_password(password):
    """
    Attempts to convert a given password/key to an integer

    Raises:
        Exception: If the function cannot cast the provided password/key to type int.
    """
    try:
        return(int(password))
    except:
        raise Exception("Key for this cipher must be an integer")


# ---- Main function to handle cli input

def main():
    """
    Handles CLI input, including commands, arguments, etc., for Bletchley.
    """
    # Create the argument parser
    parser = argparse.ArgumentParser(description="CLI for Bletchley, a cryptanalysis suite.")    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    parser.add_argument('--version', action='version', version=f'%(prog)s {__version__}')   

    frequency_parser = subparsers.add_parser("freq", help="Do frequency analysis.")
    frequency_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    frequency_parser.add_argument("-c", "--chart", choices=["c", "p", "vsbc", "vbc", "vsbca", "vbca", "vsbcar", "vbcar", "vcbcos", "vbcos", "vsbcol", "vbcol"], type=str, required=False, help="The style for the bar chart")
    
    brute_parser = subparsers.add_parser("force", help="Brute force the ciphertext knowing the cipher.")
    brute_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    brute_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to brute force")

    hash_parser = subparsers.add_parser("hash", help="Identify and reverse lookup a hash.")
    hash_parser.add_argument("-t", "--text", type=str, required=False, help="The hash to process")
    
    encoding_parser = subparsers.add_parser("decode", help="Decode a text, with or without the encoding.")
    encoding_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    encoding_parser.add_argument("-e", "--encoding", type=str, required=False, help="The encoding the text is in") # This is optional, if its not passed that means the encoding is unknown and should be found

    encoding_parser = subparsers.add_parser("encode", help="Find the encoding the text is in and/or encode the text.")
    encoding_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    encoding_parser.add_argument("-e", "--encoding", type=str, required=True, help="The encoding to encode the text with")

    learning_parser = subparsers.add_parser("classify", help="Use the machine learning model to detect which cipher was used to encrypt the text.")
    learning_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    
    run_parser = subparsers.add_parser("run", help="Try to automatically decrypt the ciphertext.")
    run_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    run_parser.add_argument("-v", "--verbose", action="store_true", help="Print the results of all tests")
    run_parser.add_argument("-w", "--wordlist", choices=["large", "small", "small_specialized", "large_specialized", "dictionary"], type=str, required=False, help="The word list to use when detecting whether a tested ciphertext is decrypted or not")

    encryption_parser = subparsers.add_parser("encrypt", help="Encrypt a text.")
    encryption_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    encryption_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to encrypt the text with")
    encryption_parser.add_argument("-p", "--password", type=str, required=False, help="The password to encrypt the text with")

    decryption_parser = subparsers.add_parser("decrypt", help="Decrypt a text.")
    decryption_parser.add_argument("-t", "--text", type=str, required=False, help="The text to process")
    decryption_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to decrypt the text with")
    decryption_parser.add_argument("-p", "--password", type=str, required=False, help="The password to decrypt the text with")

    about_parser = subparsers.add_parser("about", help="Get more information about a cipher.")
    about_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to get information about")

    # Parse the arguments
    args = parser.parse_args()

    # Handle the commands
    if args.command == "freq":
        if args.text is None:
            text = sys.stdin.read()
        else:
            text = args.text
        
        if args.chart is not None:
            frequencyAnalysis(text, args.chart)
        else:
            frequencyAnalysis(text)
    
    elif args.command == "force" or args.command == "brute":
        if args.text is None:
            text = sys.stdin.read()
        else:
            text = args.text

        if args.cipher == "caesar" or args.cipher == "1":
            force_caesar(text)

        elif args.cipher == "vigenere" or args.cipher == "2":
            force_vigenere(text)

        elif args.cipher == "atbash" or args.cipher == "4":
            force_atbash(text)


    elif args.command == "hash":
        if args.text is None:
            hash(sys.stdin.read())
        else:
            hash(args.text)


    elif args.command == "decode":
        if args.text is None:
            text = sys.stdin.read()
        else:
            text = args.text

        if args.encoding is not None:
            decode(text, args.encoding)
        else:
            auto_decode(text)


    elif args.command == "encode":
        if args.text is None:
            text = sys.stdin.read()
        else:
            text = args.text

        encode(text, args.encoding)


    elif args.command == "run":
        if args.text is None:
            text = sys.stdin.read()
        else:
            text = args.text

        if args.verbose and args.wordlist is not None:
            run(text, args.wordlist, True)
        elif args.verbose:
            run(text, "small_specialized", True)
        elif args.wordlist is not None:
            run(text, args.wordlist)
        elif text is None:
            run(sys.stdin.read(), args.wordlist)
        else:
            run(text)


    elif args.command == "encrypt" or args.command == "en" or args.command == "e":
        if args.text is None:
            text = sys.stdin.read()
        else:
            text = args.text

        if args.cipher == "caesar" or args.cipher == "1":
            check_text_password(text, args.password)
            encrypt_caesar(text, int(args.password))

        elif args.cipher == "multiplicative" or args.cipher == "14" or args.cipher == "multiplication":
            check_text_password(text, args.password)
            encrypt_multiplication(text, int(args.password))

        elif args.cipher == "vigenere" or args.cipher == "2":
            check_text_password(text, args.password)
            encrypt_vigenere(text, args.password)

        elif args.cipher == "rot13" or args.cipher == "rot" or args.cipher == "3":
            check_password_not_needed(args.password)
            encrypt_rot13(text)

        elif args.cipher == "atbash" or args.cipher == "4":
            check_password_not_needed(args.password)
            atbash(text)

        elif args.cipher == "playfair" or args.cipher == "5":
            check_text_password(text, args.password)
            encrypt_playfair(text, args.password)

        elif args.cipher == "baconian" or args.cipher == "6":
            #encrypt_baconian(STUFF HERE)
            print("I need to get the optional letter 1 and 2, and style (old or new), I could probably do this with the -p, just have them passed with commas in that")

        elif args.cipher == "affine" or args.cipher == "7":
            check_text_password(text, args.password)
            print("Decryption apparently doesn't work for this")

            if args.password.count(',') < 1:
                raise Exception("The affine cipher needs two number keys, pass them with `-p num1,num2` (with a comma)")

        elif args.cipher == "rail" or args.cipher == "rail_fence" or args.cipher == "8":
            encrypt_rail_fence(text, convert_num_password(args.password))

        elif args.cipher == "substitution" or args.cipher == "9":
            encrypt_substitution(text, args.password)

        elif args.cipher == "beaufort" or args.cipher == "10":
            encrypt_beaufort(text, args.password)

        elif args.cipher == "autokey" or args.cipher == "11":
            encrypt_autokey(text, args.password)

        elif args.cipher == "bifid" or args.cipher == "12":
            encrypt_bifid(text, args.password)

        elif args.cipher == "nonsense" or args.cipher == "15":
            nonsense(text)

        else: # MUST BE LAST IN CHAIN
            print("Please select a valid cipher (e.g. '-c caesar').")

    elif args.command == "decrypt" or args.command == "de" or args.command == "d":
        if args.text is None:
            text = sys.stdin.read()
        else:
            text = args.text

        if args.cipher == "caesar" or args.cipher == "1":
            check_text_password(text, args.password)
            decrypt_caesar(text, int(args.password))

        if args.cipher == "multiplicative" or args.cipher == "14" or args.cipher == "multiplication":
            check_text_password(text, args.password)
            decrypt_multiplication(text, int(args.password))

        elif args.cipher == "vigenere" or args.cipher == "2":
            check_text_password(text, args.password)
            decrypt_vigenere(text, args.password)

        elif args.cipher == "rot13" or args.cipher == "rot" or args.cipher == "3":
            check_password_not_needed(args.password)
            decrypt_rot13(text)

        elif args.cipher == "atbash" or args.cipher == "4":
            check_password_not_needed(args.password)
            atbash(text)

        elif args.cipher == "playfair" or args.cipher == "5":
            check_text_password(text, args.password)
            decrypt_playfair(text, args.password)

        elif args.cipher == "baconian" or args.cipher == "6":
            #decrypt_baconian(STUFF HERE)
            print("I need to get the optional letter 1 and 2, and style (old or new), I could probably do this with the -p, just have them passed with commas in that")

        elif args.cipher == "affine" or args.cipher == "7":
            check_text_password(text, args.password)
            print("Decryption apparently doesn't work for this")

            if args.password.count(',') < 1:
                raise Exception("The affine cipher needs two number keys, pass them with `-p num1,num2` (with a comma)")

        elif args.cipher == "rail" or args.cipher == "rail_fence" or args.cipher == "8":
            decrypt_rail_fence(text, convert_num_password(args.password))

        elif args.cipher == "substitution" or args.cipher == "9":
            decrypt_substitution(text, args.password)

        elif args.cipher == "beaufort" or args.cipher == "10":
            decrypt_beaufort(text, args.password)

        elif args.cipher == "autokey" or args.cipher == "11":
            decrypt_autokey(text, args.password)

        elif args.cipher == "bifid" or args.cipher == "12":
            decrypt_bifid(text, args.password)

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
