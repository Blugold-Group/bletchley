"""
This file provides funtions to brute force weak ciphers


"""

import ciphers

def ceaser(text, return_type="bg"):
    """
    Brute forces the ceaser cipher
    Takes a string text and an optional string return_type

    return_type can be: 
        bg "best guess" (the version which has the most real words in it)
        all "all" (a list of all of the possible solutions)

    In bg mode, returns the best guess, which is the string with the most instances of real words (as dictated by words.txt)
    If there are two strings with the same amount of instances 

    """

    test_texts=[]
    for i in range(1,26):
        test_texts.append(ciphers.ceaser(text, i))
    
    best_guess_string=""
    best_guess_counts=-1
    counts=[]
    for i in test_texts:
        count=0
        test=i.split()

        for j in i:
            if ciphers.is_this_real(j):
                count+=1
        if count>best_guess_counts:
            best_guess_string=i
            best_guess_counts=count
        counts.append(count)
    
    
print(ceaser("Pm ol ohk hufaopun."))