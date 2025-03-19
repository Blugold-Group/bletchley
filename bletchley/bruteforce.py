"""
Bruteforce functions for weak ciphers.

This module provides bruteforce decryption methods for various classical ciphers.
Each function attempts to decrypt ciphertexts without a key by trying all possible keys
or by using wordlists.

Returns:
    False: If the ciphertext is not encrypted with the tested cipher.
    Tuple ([plaintext, key, confidence]) if decryption is successful.
    None: If the bruteforce implementation is not yet complete.

TODO:
    - Add more ciphers
    - Allow passing of wordlist
    - Make tolerance not a global variable, passed in better
    - Write standard function for comparing a list of possible ciphertexts

For more information how the functions work, look at the Caesar function, it has comments explaining what's going on

"""

import time
from . import ciphers
import itertools
import threading
import sys
import os
from tqdm import tqdm
import importlib.resources

global tolerance
tolerance=0.65

def caesar(text, return_type="bg"):
    """
    Bruteforce decrypts a Caesar cipher.

    Args:
        text (str): The ciphertext.
        return_type (str, optional):
            - "bg" (best guess): Returns the most probable plaintext.
            - "all": Returns all possible shifts.

    Returns:
        tuple(str, int, float) | bool:
            - Best guess plaintext, key used, confidence percentage.
            - False if decryption failes.

    TODO:
        - Also return the key which was used to encrypt the text
        - Allow passing which wordlist to use

    """

    global tolerance

    # A list of the text encrypted which each possible key for caesar cipher
    test_texts=[]
    for i in range(0,26):
        test_texts.append(ciphers.caesar.decrypt(text.replace(".", "").replace(",", "").replace("'", "").lower(), i))
    
    # Creates an object for testing if a text is a word or is ciphertext
    realTest = ciphers.realEngine("small_specialized")
    
    # These two variables (best_guess) get replaced with the current tested string if the string had more real words in it that the current best_guess_count, counts is used to track how many real words are in each permutation of ciphertext
    best_guess_string=""
    best_guess_count=-1
    best_guess_key=""
    confidence=-1
    counts=[]

    for i in test_texts:
        count=0
        test=i.split()

        for j in test:
            if realTest.plaintext_or_ciphertext(j):
                count+=1
        if count>best_guess_count:
            best_guess_string=i
            best_guess_count=count
        counts.append(count)

    key = test_texts.index(best_guess_string)
    confidence = counts[test_texts.index(best_guess_string)] / (len(best_guess_string.split()))

    if realTest.plaintext_or_ciphertext(best_guess_string, tolerance):
        return(best_guess_string, key, confidence)
    return(False)
    
def vigenere(text, verbose, tolerance=0.8):
    """
    Bruteforce decrypts a Vigenère cipher using a wordlist.

    Args:
        text (str): The ciphertext.
        verbose (bool, optional): If True, prints progress during decryption.
        tolerance (float, optional): The confidence threshold for a successful decryption.

    Returns:
        tuple(str, str) | None:
            - Decrypted plaintext and key if successful.
            - None if decryption fails
    """
    
    realTest = ciphers.realEngine("small_specialized")

    with importlib.resources.open_text("bletchley", "wordlists/words.txt") as f:
        keys = [line.strip() for line in f]

    #keys = sorted(keys, key=len)

    if verbose:
        for key in tqdm(keys, desc="Brute forcing Vigenere cipher", unit="keys"):
            plaintext = ciphers.vigenere.decrypt(text, key)

            if realTest.plaintext_or_ciphertext(plaintext, tolerance):
                return(plaintext, key)

    else:
        for key in keys:
            plaintext = ciphers.vigenere.decrypt(text, key)

            if realTest.plaintext_or_ciphertext(plaintext, tolerance):
                return(plaintext, key)

def multiplication(text):
    """
    Bruteforce decrypts the Multiplication cipher.

    Args:
        text (str): The ciphertext to bruteforce.

    Returns:
        tuple(str, int, float) | bool:
            - Buest guess plainext, key used, confidence percentage.
            - False if decryption failes.
    """
    global tolerance

    keys = [ 1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]  # Only numbers less than 26 and relatively prime to 26 are possible keys, see https://www.nku.edu/~christensen/section%206%20multiplicative%20ciphers.pdf for more information)

    test_texts = []
    for i in keys:
        test_texts.append(ciphers.multiplication.decrypt(text.replace(".", "").replace(",", "").replace("'", ""), i))

    realTest = ciphers.realEngine("small_specialized")
    
    best_guess_string=""
    best_guess_count=-1
    best_guess_key=""
    confidence=-1
    counts=[]

    for i in test_texts:
        count=0
        test=i.split()

        for j in test:
            if realTest.plaintext_or_ciphertext(j):
                count+=1
        if count>best_guess_count:
            best_guess_string=i
            best_guess_count=count
        counts.append(count)

    key = keys[test_texts.index(best_guess_string)]

    
    confidence = counts[test_texts.index(best_guess_string)] / (len(best_guess_string.split()))

    if realTest.plaintext_or_ciphertext(best_guess_string, tolerance):
        return(best_guess_string, key, confidence)
    return(False)

def multiplicative(text):
    """
    Alias for multiplication().
    """
    return multiplication(text)

def substitution(text):
    """
    Bruteforces the substitution cipher.
    Takes a string text input.
    """
    #print("substitution")

    global tolerance

    return(False)

def railfence(text):
    """
    Bruteforces the Rail Fence cipher.
    Takes a string text input.
    """

    return False  # Remove this when the rail fence decryption works
    global tolerance

    realTest = ciphers.realEngine("small_specialized")

    for i in range(2,200):
        test=(ciphers.rail_fence(text, i, "d"))
        if realTest.plaintext_or_ciphertext(test, tolerance):
            return(test, i)
        
    return(False)

def playfair(text):
    """
    Bruteforces the Playfair cipher.
    Takes a string text input.
    """
    return False  # Remove this when the rail fence decryption works

def atbash(text):
    """
    Bruteforce decrypts the Atbash cipher.

    Args:
        text (str): The ciphertext.

    Returns:
        str | bool:
            - Decrypted plaintext if successful.
            - False if decryption fails.
    """
    realTest = ciphers.realEngine("small_specialized")

    test = ciphers.atbash.atbash(text)

    if realTest.plaintext_or_ciphertext(test, 0.8):
        return test

    return False

def playfair(text):
    """
    Bruteforces the Playfair cipher.
    Takes a string text input.
    """
    return False

def baconian(text):
    """
    Bruteforces Bacon's/the Baconian cipher.
    Takes a string text input.
    """
    return False

def affine(text):
    """
    Bruteforces the Affine cipher.
    Takes a string text input.
    """
    return False

def rail_fence(text):
    """
    Bruteforces the Rail Fence cipher.
    Takes a string text input.
    """
    return False

def substitution(text):
    """
    Bruteforces the substitution cipher.
    Takes a string text input.
    """
    return False

def beaufort(text):
    """
    Bruteforces the Beaufort cipher.
    Takes a string text input.
    """
    return False

def autokey(text):
    """
    Bruteforces the Autokey cipher.
    Takes a string text input.
    """
    return False

def bifid(text):
    """
    Brutefoces the Bifid cipher.
    Takes a string text input.
    """
    return False