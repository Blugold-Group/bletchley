"""
Client facing file to interface with Bletchley tools

"""

import argparse
import start
import recognizeHash

def plainFrequencyAnalysis(text):
    return("Plain frequency analysis")

def frequencyAnalysis(text, style="vbca"):
    print("Frequency analyses", style)

def hash(text):
    recognizeHash.guess(text)

def bruteForce(text, cipher):
    print("Brute force", text, cipher)

def encoding(text):
    # Decode without knowing the encoding
    print("Recognize and decode encoding")

def encode(text, encoding):
    print("Encode")

def decode(text, encoding):
    print("Decode")

def classify(text):
    return("Using ML classification to find cipher")

def run(text):
    print("Try to automatically decrypt ciphertext without key or cipher", text)

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
    frequency_parser.add_argument("-p", "--plain", action="store_true", help="Return the frequency statistics in a plain list without charts")
    frequency_parser.add_argument("-s", "--style", choices=["c", "p", "vsbc", "vbc", "vsbca", "vbca", "vsbcar", "vbcar", "vcbcos", "vbcos", "vsbcol", "vbcol"], type=str, required=False, help="The style for the bar chart")
    
    brute_parser = subparsers.add_parser("force", help="Brute force the ciphertext knowing the cipher.")
    brute_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    brute_parser.add_argument("-c", "--cipher", type=str, required=True, help="The cipher to brute force")

    hash_parser = subparsers.add_parser("hash", help="Identify and reverse lookup a hash.")
    hash_parser.add_argument("-t", "--text", type=str, required=True, help="The hash to process")
    
    encoding_parser = subparsers.add_parser("decode", help="Find the encoding the text is in and/or decode the text.")
    encoding_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    encoding_parser.add_argument("-e", "--encoding", type=str, required=False, help="The encoding the text is in") # This is optional, if its not passed that means the encoding is unknown and should be found
    
    learning_parser = subparsers.add_parser("classify", help="Use the machine learning model to detect which cipher was used to encrypt the text.")
    learning_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")
    
    run_parser = subparsers.add_parser("run", help="Try to automatically decrypt the ciphertext.")
    run_parser.add_argument("-t", "--text", type=str, required=True, help="The text to process")


    # Parse the arguments
    args = parser.parse_args()

    # Handle the commands
    if args.command == "freq":
        if args.plain:
            print(plainFrequencyAnalysis(args.text))
        else:
            print("Charts")
            if args.style is not None:
                frequencyAnalysis(args.text, args.style)
            else:
                frequencyAnalysis(args.text)
    
    elif args.command == "force":
        bruteForce(args.text, args.cipher) # This will run for a while depending on how long, it should run a loading icon while working
    
    elif args.command == "hash":
        hash(args.text)

    elif args.command == "decode":
        result = to_uppercase(args.text)
        print(f"Uppercase text: {result}")

    elif args.command == "classify":
        result = classify(args.text)
        print(f"Uppercase text: {result}")

    elif args.command == "run":
        run(args.text)
    
    else:
        help()


if __name__ == "__main__":
    main()
