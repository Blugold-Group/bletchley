"""
Client facing file to interface with Bletchley tools

The first argument must be the ciphertext (unless -h or --help is the first argument)

Format is "Bletchley.py "ciphertexthere" -options

If no flags are passed, frequency analysis and then automatic decryption is run

Options are:
    -f frequency analysis
        Prints the raw frequency of the text

    -fv frequency analysis verbose
        Prints charts of the frequency analysis

    -b brute force
        Brute forces a given text

    -hc hash crack
        Returns a command to use with hashcat to crack the given hash

    -hr hash recognize
        Tries to recognize the given hash

    -e encoding 
        Attempts to recognize and decode a string with encoding standards

            -s [blank] standard 
                Attempts to decode with the given standard

            -r [blank] rounds
                Tries to decode the string r times over (in case a string is encoding multiple times with the same encoding)

    -g [blank] guess
        Returns the best guess for which cipher was used to encrypt a given ciphertext. Not recomended because not all ciphers are included in the model


"""

import sys
import start

argsnum = len(sys.argv)
bruteforce=False
hashcrack=False

if argsnum > 1:

    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("Help here")
        exit()

    ciphertext = sys.argv[1]

    if argsnum == 2:
        # Just a ciphertext passed, runs automatic decryption
        start.run(ciphertext)
    
    # Accessing subsequent arguments in a similar way
    for i in range(2, len(sys.argv)):
        if bruteforce == True:
            if "v" in i:
                print("vigenere")
            elif "c" in i:
                print("caesar")
            elif "af" in i:
                print("atbash")

            bruteforce=False

        elif sys.argv[i] == "-f":
            # Frequency analysis
            print("Frequency anlysys")

        elif sys.argv[i] == "-fv":
            # Frequency analysis verbose
            print("Frequency analysis with charts")

        elif sys.argv[i] == "-hc":
            # Hash crack
            print("Hash crack")
            hashcrack=True
        
        elif sys.argv[i] == "-hr":
            # Hash Recognize
            print("Hash recognize")

        elif sys.argv[i] == "-b":
            # Brute force
            print("Brute force")
            bruteforce=True

        elif sys.argv[i] == "-e":
            # Encoding
            print("Recognize and decode encoding")

        elif sys.argv[i] == "-g":
            # Guess
            print("Guess which cipher was used using ml model")

else:
    print("No arguments provided.")
