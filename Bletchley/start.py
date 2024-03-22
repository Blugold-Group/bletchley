"""
The first things ran against a ciphertext

1. Cheap brute forcing
    - Caesar
    - Rot13
    - Substitution

2. Machine Learning guess

3. Brute force the best guess


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

    # ML Guess what the cipher is
    predicted=predict.predict_cipher(ciphertext)
    if predicted == "vigenere":
        bruteforce.vigenere(ciphertext)


run(ciphers.rot13("Hello world"))