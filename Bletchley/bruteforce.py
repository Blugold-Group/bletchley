"""
This file provides funtions to brute force weak ciphers


"""

import ciphers

def caesar(text, return_type="bg"):
    """
    Brute forces the caesar cipher
    Takes a string text and an optional string return_type

    return_type can be: 
        bg "best guess" (the version which has the most real words in it)
        all "all" (a list of all of the possible solutions)

    In bg mode, returns the best guess, which is the string with the most instances of real words (as dictated by words.txt)
    If there are two strings with the same amount of instances 

    TODO:
        - Also return the key which was used to encrypt the text

    """

    # A list of the text encrypted which each possible key for caesar cipher
    test_texts=[]
    for i in range(1,26):
        test_texts.append(ciphers.caesar(text, i))
    
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
            if realTest.is_this_real(j):
                count+=1
        if count>best_guess_count:
            best_guess_string=i
            best_guess_count=count
        counts.append(count)

    return(best_guess_string)
    