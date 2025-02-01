"""
This file provides functions to brute force weak ciphers

All brute force methods need to be able to work with spaces and no spaces

All brute force methods return False if the ciphertext isn't encrypted with that cipher, the [ciphertext, key, percentage_words] if automatic solving worked, and None if the brute forcing isn't implemented yet

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

global tolerance
tolerance=0.8

def caesar(text, return_type="bg"):
    """
    Brute forces the caesar cipher
    Takes a string text and an optional string return_type

    return_type can be: 
        bg "best guess" (the version which has the most real words in it)
        all "all" (a list of all of the possible solutions)

    In bg mode, returns the best guess, which is the string with the most instances of real words
    If there are two strings with the same amount of instances 

    TODO:
        - Also return the key which was used to encrypt the text
        - Allow passing which wordlist to use

    """

    global tolerance

    # A list of the text encrypted which each possible key for caesar cipher
    test_texts=[]
    for i in range(0,26):
        test_texts.append(ciphers.caesar.decrypt(text.replace(".", "").replace(",", "").replace("'", ""), i))
    
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
    Brute forces the vigenere cipher, using a wordlist as the list of keys
    """
    
    realTest = ciphers.realEngine("small_specialized")

    with open("wordlists/words.txt", 'r') as file:
        keys = [line.strip() for line in file]

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
    return multiplication(text)

def substitution(text):
    #print("substitution")

    global tolerance

    return(False)

def railfence(text):

    return False  # Remove this when the rail fence decryption works
    global tolerance

    realTest = ciphers.realEngine("small_specialized")

    for i in range(2,200):
        test=(ciphers.rail_fence(text, i, "d"))
        if realTest.plaintext_or_ciphertext(test, tolerance):
            return(test, i)
        
    return(False)

def playfair(text):
    return False  # Remove this when the rail fence decryption works

def atbash(text):

    realTest = ciphers.realEngine("small_specialized")

    test = ciphers.atbash(text)

    if realTest.plaintext_or_ciphertext(test, 0.8):
        return test

    return False

def playfair(text):
    return False

def baconian(text):
    return False

def affine(text):
    return False

def rail_fence(text):
    return False

def substitution(text):
    return False

def beaufort(text):
    return False

def autokey(text):
    return False

def bifid(text):
    return False