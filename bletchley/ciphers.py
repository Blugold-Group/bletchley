"""
Provides encryption and decryption functions for ciphers

Style:
    - Cases, spaces, and punctuation are preserved whenever possible
    - Spaces and punctuations are skipped when ran through the algorithm
    - Special characters not being an uppercase or lowercase letters may be changed to best fit into the alphabet (IE ù will be replaced with u)

TODO:
    - Add an option to ignore special characters in frequency analysis
    - Add options to frequency analysis to display analysis from most to least frequent, vice versa, or alphabetical order 
    - Allow realEngine to work with sentences not separated by spaces
    - Add a standardized text cleaning function

"""

import random
import string
from faker import Faker
import re 
import json
from random import randrange
from itertools import chain, cycle


global lower_alphabet
global upper_alphabet
global alphabet
global punctuation
global numbers

lower_alphabet="abcdefghijklmnopqrstuvwxyz"
upper_alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet=lower_alphabet+upper_alphabet
punctuation=".,></;:'[]!@#$%^&*()—-_=+`~|\"\\"
numbers="1234567890"

faker = Faker()

class realEngine:
    def __init__(self, corpus="small_specialized"):

        if corpus=="large":
            f = open("wordlists/words_dictionary.json", "r")
            self.data = json.load(f)
            f.close()
        elif corpus=="small":
            with open("wordlists/words.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="small_specialized":
            with open("wordlists/words_specialized.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="large_specialized":
            with open("wordlists/words_dictionary_specialized.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="dictionary":
            with open("wordlists/dictionary.txt") as f:
                self.data = f.read().splitlines() 
            f.close()

        self.corpus=corpus

    def is_this_real(self, word):
        word=word.lower()

        if word in self.data:
            return True
        else:
            return False
    
    def plaintext_or_ciphertext(self, sentence, tolerance=0.51):
        """
        A method to determine if a string is english 

        The tolerance is the percentage/100 of the text which has to be english words in order to be labelled as "real"

        Sentences are determined by splitting the sentence by spaces
        """
        words=sentence.split()
        length=len(words)
        count=0
        for i in words:
            #if len(i)>1:
            if self.is_this_real(i):
                count+=1
        
        if count/length>=tolerance:
            return True
        return False

def process_text(text: str):
    """
    Processes the input text by separating alphanumeric characters from punctuation, spaces, and capitalization.

    Args:
        text (str): The input text to process.

    Returns:
        tuple: A tuple containing three elements:
            - stripped_text (str): The text with all punctuation and spaces removed.
            - punctuation_map (list): A list of tuples, each containing the index and character
              of punctuation or space in the original text.
            - capitalization_map (list): A list of boolean values indicating if each character
              in the stripped text was uppercase in the original text.
    """
    punctuation_map = [(i, char) for i, char in enumerate(text) if char in string.punctuation + " "]
    stripped_text = ''.join(char for char in text if char.isalnum())
    capitalization_map = [char.isupper() for char in stripped_text]
    stripped_text = stripped_text.lower()
    return stripped_text, punctuation_map, capitalization_map

def reinflate(ciphertext: str, punctuation_map: list, capitalization_map: list):
    """
    Reinserts punctuation, spaces, and capitalization into the ciphertext based on the original text's maps.

    Args:
        ciphertext (str): The text after ciphering, without punctuation or spaces.
        punctuation_map (list): A list of tuples, each containing the index and character
                                of punctuation or space in the original text.
        capitalization_map (list): A list of boolean values indicating if each character
                                   in the stripped text was uppercase in the original text.

    Returns:
        str: The ciphertext with punctuation, spaces, and capitalization reinserted.
    """
    cipher_chars = list(ciphertext)
    for i, is_upper in enumerate(capitalization_map):
        if is_upper:
            cipher_chars[i] = cipher_chars[i].upper()

    for index, char in punctuation_map:
        cipher_chars.insert(index, char)

    return ''.join(cipher_chars)

def caesar(text, increment=randrange(1,26)):
    # Caesar Cipher https://en.wikipedia.org/wiki/Caesar_cipher

    global lower_alphabet
    global upper_alphabet
    global alphabet

    encrypted=""

    text, punctuation_map, capitalization_map = process_text(text)

    for i in text:
        if i in upper_alphabet:
            letter_index=upper_alphabet.index(i)+increment
            letter_index=letter_index%26
            encrypted+=upper_alphabet[letter_index]
        elif i in lower_alphabet:
            letter_index=lower_alphabet.index(i)+increment
            letter_index=letter_index%26
            encrypted+=lower_alphabet[letter_index]

    return reinflate(encrypted, punctuation_map, capitalization_map)

def rot13(text, mode="e"):
    # Increments the text by 13
    # Leaves spaces, punctuation, and numbers alone. Breaks with special characters

    global punctuation
    global lower_alphabet
    global upper_alphabet
    global alphabet
    global numbers

    encrypted=""

    if mode=="e":
        for i in text:
            if i in punctuation or i in numbers or i == " ":
                encrypted+=i
                continue
            elif i in upper_alphabet:
                letter_index=upper_alphabet.index(i)+13
                letter_index=letter_index%26
                encrypted+=upper_alphabet[letter_index]
            elif i in lower_alphabet:
                letter_index=lower_alphabet.index(i)+13
                letter_index=letter_index%26
                encrypted+=lower_alphabet[letter_index]

    if mode=="d":
        for i in text:
            if i in punctuation or i in numbers or i == " ":
                encrypted+=i
                continue
            elif i in upper_alphabet:
                letter_index=upper_alphabet.index(i)-13
                letter_index=letter_index%26
                encrypted+=upper_alphabet[letter_index]
            elif i in lower_alphabet:
                letter_index=lower_alphabet.index(i)-13
                letter_index=letter_index%26
                encrypted+=lower_alphabet[letter_index]

    return(encrypted)

def vigenere(text, password=faker.word(), mode="e"):
    # The vigenere cipher

    global lower_alphabet
    global upper_alphabet
    #text=''.join(e for e in text if e.isalnum())
    text=text.replace("ù", "u").replace("é", "e").replace("æ", "ae").replace("ê", "e").replace("è", "e").replace("ç", "c").replace("ô", "o")
    #text=re.sub(r'\d+', '', text)

    encrypted=""
    passIndex=0


    for i in text:
        if i not in lower_alphabet and i not in upper_alphabet:
            encrypted+=i
            continue

        value = lower_alphabet.index(i.lower())
        try:
            if mode=="d":
                if i in lower_alphabet:
                    value = (value-lower_alphabet.index(password[passIndex].lower()))
                    if value<0: # If value is a negative number, wrap around the alphabet
                        value+=26
                else:
                    value = (value-upper_alphabet.index(password[passIndex].lower()))
                    if value<0: # If value is a negative number, wrap around the alphabet
                        value+=26
            else:
                value = (value+lower_alphabet.index(password[passIndex].lower()))%26
        except:
            print("~~~ Failed ~~~")
            print(password)
            print(passIndex)
            print(text)
            print("===========\n\n")

            value=1

        if i in lower_alphabet:
            encrypted+=lower_alphabet[value]
        else:
            encrypted+=upper_alphabet[value]

        if passIndex==len(password)-1:
            passIndex=0
        else:
            passIndex+=1

    return(encrypted)

def playfairFormat(text):
    text = text.lower()
    temp = ""
    for i in text:
        if i == " ":
            continue
        else:
            temp+=i
    text = temp
    temp = ""
    for index, i in enumerate(text):
        if index == 0:
            continue
        if index % 2 == 0:
            temp+= " "
        else:
            temp+=text[index-1]
            temp+=i
    text = temp

    if len(text) % 2 == 1:
        text+="z"
    
    return text

def playfairDiagraph(key):
    diagraphText = lower_alphabet.replace('j','-')
    key = key.lower()
    print(list(diagraphText))
    diagraph=['' for i in range(5)]

    i=0;j=0

    for char in key:
        if char in diagraphText:
            diagraph[i]+=char
            diagraphText=diagraphText.replace(char,'-')

            j+=1

            if j>4:
                i+=1
                j=0

    for char in diagraphText:
        if char != '-':
            diagraph[i]+=char

            j+=1

            if j>4:
                i+=1
                j=0
        
    return(diagraph)

def playfairDecryption(text,keyMatrix):

    textPairs = []
    
    for i in range(len(text)):
        if i == " ":
            a=text[i-2]
            b=text[i-1]
            textPairs.append(a+b)

            i+=2
        
def playfair(text, key='monarchy'):
    text = playfairFormat(text)
    keyMatrix = playfairDiagraph(key)

def atbash(text):
    global lower_alphabet
    global upper_alphabet
    encrypted=""

    for i in text:
        if i in lower_alphabet:
            encrypted+=lower_alphabet[25-lower_alphabet.index(i)]
        elif i in upper_alphabet:
            encrypted+=upper_alphabet[25-upper_alphabet.index(i)]
        else:
            encrypted+=i
    
    return(encrypted)

def baconian(text, mode="e", l1="a", l2="b", style="old"):
    """
    Baconian cipher

    Ignores non alphabetic characters, cipher doesn't differentiate between cases, so everything is treated as lowercase

    There are two versions, old and new
        - The old version translates (i and j) and (u and v) to the same binary representation 
        - The new version doesn't do any of that nonsense

    There is some more to the Baconian cipher, something about typefaces, but that's not included in this implementation

    See https://en.wikipedia.org/wiki/Bacon's_cipher for details
    """

    global lower_alphabet
    global upper_alphabet
    encrypted=""
    text=text.lower()

    for i in text:
        bacon=""
        if i not in lower_alphabet:
            continue
        else:
            ind=lower_alphabet.index(i)
            if style=="old":
                if ind > 20:
                    ind-=2
                elif ind > 8:
                    ind-=1
            binary = "{0:b}".format(int(ind))
        for j in binary:
            if j=="0":
                bacon+=l1
            if j=="1":
                bacon+=l2
        while len(bacon)<5:
            bacon="a"+bacon

        encrypted+=bacon+" "

    return(encrypted[:-1])

def affine(text, key1=randrange(1,25), key2=randrange(1,25), mode="e"):
    """
    Affine cipher
    
    Ignores non alphabetic characters and preserves cases

    mode
        - e = encryption
        - d = decryption

    TODO:
        - Make decryption work
    """

    global lower_alphabet
    global upper_alphabet
    encrypted=""

    for i in text:
        if i.lower() in lower_alphabet:
            if mode=="e":
                index=((key1*lower_alphabet.index(i.lower())) + key2) % 26
            elif mode=="d":
                index=((lower_alphabet.index(i.lower())) + key2) % 26

            if i in lower_alphabet:
                encrypted+=lower_alphabet[index]
            else:
                encrypted+=upper_alphabet[index]
        else:
            encrypted+=i
            continue

    return(encrypted)

def rail_fence(text, n=randrange(2,7), mode="e"):
    print("Rail fence also has an option for an offset, add that")
    
    if n < 2:
        raise Exception("Rail fence requires a key above 1") 
    
    fence = []
    rail = 0
    index = 1
    toReturn = ""

    if mode == "e":
        for i in range(n):
            fence.append([])

        for character in text:
            fence[rail].append(character)
            rail+=index

            if rail == n-1 or rail == 0:
                index = -index

        for i in fence:
            for j in i:
                toReturn += j

    elif mode == "d":
        reverseFence = []

        for i in range(n):
            fence.append([])
            reverseFence.append([])

        for character in text:
            fence[rail].append(character)
            rail+=index

            if rail == n-1 or rail == 0:
                index = -index

        i = 0
        length = len(text)
        text = list(text)
        for k in fence:
            for j in range(len(k)):
                reverseFence[i].append(text[0])
                text.remove(text[0])
            i += 1

        rail = 0
        index  = 1

        for i in range(length):
            toReturn += reverseFence[rail][0]
            reverseFence[rail].remove(reverseFence[rail][0])
            rail += index

            if rail == n-1 or rail == 0:
                index = -index

    return toReturn

def substitution(text):
    return("Add substitution here")

def beaufort(plaintext, key):
    # Beaufort Cipher

    plaintext, punctuation_map, capitalization_map = process_text(plaintext)

    global lower_alphabet
    key = key.lower()

    ciphertext = ""
    key_length = len(key)

    for i, char in enumerate(plaintext):
        if char in lower_alphabet:
            key_char = key[i % key_length]
            char_index = lower_alphabet.index(char)
            key_index = lower_alphabet.index(key_char)
            encrypted_index = (key_index - char_index) % len(lower_alphabet)
            ciphertext += lower_alphabet[encrypted_index]

    return reinflate(ciphertext, punctuation_map, capitalization_map)

