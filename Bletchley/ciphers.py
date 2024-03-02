"""
This file provides the backend of ciphers. 

Cases are preserved where possible

This file was reused from an old file, some of the functions might not fit the same coding style and may need to be deleted or rewritten

TODO:
    - vigenere_backend doesn't preserve cases, numbers, or punctuation
    - Get rid of unessecary funtions from old project
    - Add an option to ignore special charcetrs in frequency analysis
    - Add iptions to frequency analysis to display analysis from most to least frequent, vice versa, or alphabetical order 
    - Add option to combine upper and lowercase letters

"""

import random
from faker import Faker
import re 
import json
from random import randrange

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

def caesar(text, increment=randrange(1,27)):
    # Increments the text based on the increment
    # Leaves spaces, punctuation, and numbers alone. Breaks with special characters

    global punctuation
    global lower_alphabet
    global upper_alphabet
    global alphabet
    global numbers

    encrypted=""

    for i in text:
        if i in punctuation:
            encrypted+=i
            continue
        elif i in numbers:
            encrypted+=i
            continue
        elif i == " ":
            encrypted+=i
            continue
        elif i in upper_alphabet:
            letter_index=upper_alphabet.index(i)+increment
            letter_index=letter_index%26
            encrypted+=upper_alphabet[letter_index]

        elif i in lower_alphabet:
            letter_index=lower_alphabet.index(i)+increment
            letter_index=letter_index%26
            encrypted+=lower_alphabet[letter_index]
    return(encrypted)


def password():
    # Returns a random word of 10 characters or longer (usually for a password)

    password=""
    while len(password)<9:
        password=faker.word()
    return((password).lower())

def randomText(length):
    # Returns a string of (length) random letters

    global lower_alphabet
    random_sentence = ''.join(random.choices(lower_alphabet, k=length))
    return random_sentence

def randomTextRandomLength(start=1, stop=50):
    # Returns randomText with a random length (length defaults to somewhere between 1 and 50)

    length=random.randint(start, stop)
    return(randomText(length))

def vigenere(text, password=faker.word()):
    # The vigenere cipher

    global lower_alphabet
    text=''.join(e for e in text if e.isalnum())
    text=text.replace("ù", "u").replace("é", "e").replace("æ", "ae").replace("ê", "e").replace("è", "e").replace("ç", "c").replace("ô", "o")
    text=re.sub(r'\d+', '', text)
    text=text.lower()

    encrypted=""
    passIndex=0

    for i in text:
        value = lower_alphabet.index(i)
        value = (value+lower_alphabet.index(password[passIndex]))%26
        encrypted+=lower_alphabet[value]
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




def frequencyAnalysis(text):
    # Performs frequency analysis on a text and displays it in graphs
    import plotext as plt


    foundCharacters=[]
    counts=[]

    for i in text:
        if i not in foundCharacters:
            foundCharacters.append(i)
            counts.append(1)
        else:
            counts[foundCharacters.index(i)]+=1
    
    print(foundCharacters)
    print(counts)

    plt.bar(foundCharacters, counts)
    plt.title("Frequency Analysis")
    plt.show()
