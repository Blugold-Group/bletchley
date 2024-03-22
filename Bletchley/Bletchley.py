"""
Client facing file to interface with Bletchley tools

The first argument must be the ciphertext

"""

import sys
import start

argsnum = len(sys.argv)
bruteforce=False

if argsnum > 1:
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

        elif i == "-f":
            # Frequency analysis
            print("Frequency anlysys")

        elif i == "-fv":
            # Frequency analysis verbose
            print("Frequency analysis with charts")
        
        elif i == "-b":
            # Brute force
            print("Brute force")
            bruteforce=True

        elif i == "-hc":
            # Hash crack
            print("Hash crack")
        
        elif i == "-hr":
            # Hash Recognize
            print("Hash recognize")

        elif i == "-e":
            # Encoding
            print("Recognize and decode encoding")

        elif i == "-g":
            # Guess
            print("Guess which cipher was used using ml model")

        





        print(f"Argument {i}:", sys.argv[i])
else:
    print("No arguments provided.")
