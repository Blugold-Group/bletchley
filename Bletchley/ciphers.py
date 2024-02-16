# Provides vigenere cipheretext based on random word keys and text from books
# For each ciphertext it returns. it also returns a random string of the same length
# All characters are lowercase

import random
import string
import os
from faker import Faker
import re 
import json


faker = Faker()

def is_this_real(text):
    # This function is used to determine if decrypted text is still ciphertext or a real sentence

    f = open("words_dictionary.json", "r")

    data = json.load(f)
    print(data)

    f.close()

is_this_real("wfebwjebfjwef")


def password():
    password=""
    while len(password)<9:
        password=faker.word()
    return((password).lower())

def randome(length):
    lowercase_letters = string.ascii_lowercase
    random_sentence = ''.join(random.choices(lowercase_letters, k=length))
    return random_sentence

def randomText():
    length=random.randint(1,50)
    return(randome(length))

def vigenere_backend(text):
    text=''.join(e for e in text if e.isalnum())
    text=text.replace("ù", "u").replace("é", "e").replace("æ", "ae").replace("ê", "e").replace("è", "e").replace("ç", "c").replace("ô", "o")
    text=re.sub(r'\d+', '', text)
    text=text.lower()


    passw=password()
    alphabet="abcdefghijklmnopqrstuvwxyz"
    encrypted=""
    passIndex=0

    for i in text:
        value = alphabet.index(i)
        value = (value+alphabet.index(passw[passIndex]))%26
        encrypted+=alphabet[value]
        if passIndex==len(passw)-1:
            passIndex=0
        else:
            passIndex+=1

    return(encrypted)

def vigenere():
    f=open("quotes.csv", "r")
    quotes=f.readlines()
    for i in quotes:
        print(vigenere_backend(i))
    f.close()

def randomSentence():
    book=random.choice(os.listdir('texts'))
    with open("texts/"+book) as f:
        lines = f.readlines()
    return(random.choice(lines))

def ciphertext():
    line=""
    while line=="" or line=="\n" or line==" " or len(line)<5:
        line=randomSentence()
    return vigenere(line)

def randomData():
    ciph=ciphertext()
    length=len(ciph)
    return(ciph, randome(length))
