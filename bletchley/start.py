"""
The first things ran against a ciphertext

1. Cheap brute forcing
    - Caesar
    - Rot13
    - Substitution
    - Atbash

2. Machine Learning guess

3. Brute force the best guess

TODO:
    - Don't make finding one option end the script, try them all and return all results

    
"""

import ciphers
import bruteforce

def test_failed(test, verbose):
    # The logging utility for a failed test
    if verbose:
        print("Test ", test, ": failed")

def info(text):
    print("Info:  ", text)

def run(ciphertext, wordlist="small_specialized", verbose=False):
    # Start an engine for determining if a string is decrypted
    realTest = ciphers.realEngine(wordlist)

    # Brute force easy ciphers
    test=ciphers.rot13(ciphertext)
    if (realTest.plaintext_or_ciphertext(test, 0.8)):
        print("Rot13 :", ciphers.rot13(ciphertext))
        return
    test_failed("Rot13", verbose)

    test=bruteforce.caesar(ciphertext)
    if (test):
        print("Caesar :", test)
        return
    test_failed("Caesar Cipher", verbose)

    test=bruteforce.railfence(ciphertext)
    if (test):
        print("Railfence :", test[0], "key :", test[1])
        return
    test_failed("Rail Fence", verbose)

    test=bruteforce.substitution(ciphertext)
    if (test):
        print("Substitution :", test)
        return
    test_failed("Substitution Cipher", verbose)

    test=ciphers.atbash(ciphertext)
    if (realTest.plaintext_or_ciphertext(test, 0.8)):
        print("Atbash :", test)
        return
    test_failed("Atbash Cipher", verbose)

    info("Starting machine learning analysis")

    # ML Guess what the cipher is
    predicted=predict.predict_cipher(ciphertext)

    con=input("Found "+predicted+", do you want to run automatic decryption?  ")
    if con=="y":
        if predicted == "vigenere":
            bruteforce.vigenere(ciphertext)
        if predicted == "baconian":
            print("Enter decyrption here")
            #print(ciphers.baconian(ciphertext))



#ciphertexts=["Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.", "Zrc kewsg npaov hat beqfu ajcp zrc lidy xam.", "Twt byirz mvolc qsx yjxts dkpv twt wezn szk.", "baaba aabbb aabaa abbbb baabb abaaa aaaba abaab aaaab baaaa abbab babaa abbaa aabab abbab babab abaaa baabb ababb abbba baaab abbab baabb aabaa baaaa baaba aabbb aabaa ababa aaaaa babbb babba aaabb abbab aabba", "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.", "arIhtad  tete ?t  ahoehyjc fsorekr iuod edwgtiava hs teret w  th aoduhtn uao  otluwypstodon lu,n y eao  t hvgiiselaetl"]

#for i in ciphertexts:
#    run(i)

