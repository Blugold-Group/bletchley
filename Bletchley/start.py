"""
The first things ran against a ciphertext

1. Cheap brute forcing
    - Caesar
    - Rot13
    - Substitution

2. Machine Learning guess

3. Brute force the best guess

TODO:
    - Don't make finding one option end the script, try them all and return all results

    
"""

import ciphers
import predict
import bruteforce

def run(ciphertext):
    # Start an engine for determining if a string is decrypted
    realTest = ciphers.realEngine("small_specialized")

    # Brute force easy ciphers
    test=ciphers.rot13(ciphertext)
    if (realTest.plaintext_or_ciphertext(test, 0.8)):
        print("Rot13 :", ciphers.rot13(ciphertext))
        exit()

    test=bruteforce.caesar(ciphertext)
    if (test):
        print("Caesar :", test)
        exit()

    test=bruteforce.substitution(ciphertext)
    if (test):
        print("Substitution :", test)
        exit()

    test=ciphers.atbash(ciphertext)
    if (realTest.plaintext_or_ciphertext(test, 0.8)):
        print("Atbash :", test)
        exit()

    print("Starting machine learning analysis")

    # ML Guess what the cipher is
    predicted=predict.predict_cipher(ciphertext)
    if predicted == "vigenere":
        bruteforce.vigenere(ciphertext)

    print(predicted)



run(ciphers.atbash("attack at dawn"))