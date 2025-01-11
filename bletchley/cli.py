"""
Client facing file to interface with Bletchley tools

"""

import argparse
import start
import recognizeHash
import frequency
import encodings

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

def encrypt(text, cipher, password):
    print("encrypt")

def decrypt(text, cipher, password):
    print("encrypt")


def main():
    # Create the argument parser
    parser = argparse.ArgumentParser(description="CLI for Bletchley, a cryptanalysis suite.")    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
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
    
    else:
        help()


if __name__ == "__main__":
    main()
