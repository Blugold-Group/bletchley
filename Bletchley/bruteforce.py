"""
This file provides funtions to brute force weak ciphers

All brute force methods need to be able to work with spaces and no spaces

TODO:
    - Add threaading on Vigenere brute force (caesar probably doesn't need it)

"""

import ciphers
from english_dictionary.scripts.read_pickle import get_dict

def ceaser(text, return_type="bg"):
    """
    Brute forces the ceaser cipher
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

    # A list of the text encrypted which each possible key for ceaser cipher
    test_texts=[]
    for i in range(1,26):
        test_texts.append(ciphers.ceaser(text, i))
    
    # Creates an object for testing if a text is a word or is ciphertext
    realTest = ciphers.realEngine("small_specialized")
    
    # These two variables (best_guess) get replaced with the current tested string if the string had more real words in it that the current best_guess_count, counts is used to track how many real words are in each permutation of ciphertext
    best_guess_string=""
    best_guess_count=-1
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

    return(best_guess_string)
    
def vigenere(text):
    count=0
    decrypted=False
    decryptedText=[]
    keys=[]
    english_dict = get_dict()
    realTest = ciphers.realEngine("small_specialized")

    for i in english_dict:
        count+=1

        if len(i)>0:
            print(str(count+1)+" / "+str(len(english_dict)))
            i=i.lower()
            
            if (realTest.plaintext_or_ciphertext(ciphers.vigenere(text, i, "d"))):
                decrypted=True
                decryptedText.append(ciphers.vigenere(text, i, "d"))
                keys.append(i)

    if decrypted:
        if len(keys)>1:
            print("Found", str(len(keys)), "combinations")
        else:
            print("Found 1 combination")

        for text, key in zip(decryptedText, keys):
            print(key, ": ", text)
    else:
        print("Nothing found")


vigenere("Twt byirz")