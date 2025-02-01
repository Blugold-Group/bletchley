"""
Provides encryption and decryption functions for ciphers

TODO:
    - Add options to frequency analysis to display analysis from most to least frequent, vice versa, or alphabetical order 
    - Allow realEngine to work with sentences not separated by spaces
    - Standardize ciphers to use the input text plaintext or ciphertext (not text or message)
    - Add baconian cipher decryption
    - Add stuff for python linters, input and outputs params for functions and file
    - Remove global variable, use a better standardized method across ciphers
    - Rework the wordlists for realEngine, make sure they're high quality, make them a better/faster/standardized format, and get better measurements on them (size/efficacy)
    - Add more ciphers
    - Make all ciphers use plaintext and ciphertext for encrypt() and decrypt() functions

"""

import random
import string
from faker import Faker
import re 
import json
from random import randrange
from itertools import chain, cycle
import importlib.resources

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
            with importlib.resources.open_text("bletchley", "wordlists/words_dictionary.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="small":
            with importlib.resources.open_text("bletchley", "wordlists/words.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="small_specialized":
            with importlib.resources.open_text("bletchley", "wordlists/words_specialized.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="large_specialized":
            with importlib.resources.open_text("bletchley", "wordlists/words_dictionary_specialized.txt") as f:
                self.data = f.read().splitlines() 
            f.close()
        elif corpus=="dictionary":
            with importlib.resources.open_text("bletchley", "wordlists/dictionary.txt") as f:
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
        else:
            cipher_chars[i] = cipher_chars[i].lower()

    for index, char in punctuation_map:
        cipher_chars.insert(index, char)

    return ''.join(cipher_chars)

def verify_input(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        raise ValueError("text is empty")

def verify_key_exists(text):
    if not isinstance(text, str):
        raise TypeError("Key must be a string")
    if not text:
        raise ValueError("You have to pass a key")

def verify_int_key(key):
    if not isinstance(key, int):
        raise TypeError("key must be an integer")
    if not key and key=="0":
        raise ValueError("key is empty")

class template:
    @staticmethod
    def about():
        return "A little blurb about the cipher and how it works"

    @staticmethod
    def encrypt(plaintext, key):
        return "Encrypt a text"

    @staticmethod
    def decrypt(ciphertext, key):
        return "Decrypt a text"

    @staticmethod
    def extra(text, key):
        return "Internal functions for use by the cipher"

class caesar:
    @staticmethod
    def about(useRot13=False):
        if(useRot13):
            return ("ROT13 cipher https://en.wikipedia.org/wiki/ROT13 \n"
                    "This is a simple subsitution cipher, replacing the input letter with "
                    "an output letter offset by 13 places (e.g. 'A' becomes 'N', 'B' becomes 'O', etc.)"
                    "The ROT13 cipher is simply the Caesar cipher with a key-value of 13. ")
        else:
            return ("Caesar cipher https://en.wikipedia.org/wiki/Caesar_cipher \n"
                    "This is a simple substitution cipher, replacing the input letter with "
                    "an output letter offset by a set number of places.")

    @staticmethod
    def encrypt(text, increment=randrange(1,26)):
        global lower_alphabet
        global upper_alphabet
        global alphabet

        verify_int_key(increment)

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

    @staticmethod
    def decrypt(text, increment=randrange(1,26)):
        return caesar.encrypt(text, -increment)

class playfair:
    @staticmethod
    def about():
        return ("Playfair cipher: https://en.wikipedia.org/wiki/Playfair_cipher\n"
                "This cipher encrypts text in letter pairs using a 5x5 key matrix, "
                "replacing 'J' with 'I' and inserting 'X' between duplicate letters or "
                "at the end of the message to maintain an even number of characters. "
                "Decryption preserves these alterations, which may lead to unexpected output.")

    @staticmethod
    def prepare_text(text):
        text = text.upper().replace("J", "I").replace(" ", "")
        prepared_text = ""

        i = 0
        while i < len(text):
            a = text[i]
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    prepared_text += a + 'X'
                    i += 1
                else:
                    prepared_text += a + b
                    i += 2
            else:
                prepared_text += a + 'X'
                i += 1

        return prepared_text

    @staticmethod
    def generate_key_matrix(key):
        key = key.upper().replace("J", "I").replace(" ", "")
        key_set = set()
        matrix = []
        alphabet = string.ascii_uppercase.replace("J", "")  # No 'J' in Playfair

        for char in key + alphabet:
            if char not in key_set:
                key_set.add(char)
                matrix.append(char)

        return [matrix[i:i + 5] for i in range(0, 25, 5)]  # Converting to th e5x5 format

    @staticmethod
    def find_position(matrix, char):
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return None

    @staticmethod
    def encrypt(text, key_matrix):
        text = playfair.prepare_text(text)
        encrypted_text = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]
            row_a, col_a = playfair.find_position(key_matrix, a)
            row_b, col_b = playfair.find_position(key_matrix, b)

            if row_a == row_b:  # Same row: shift right
                encrypted_text += key_matrix[row_a][(col_a + 1) % 5]
                encrypted_text += key_matrix[row_b][(col_b + 1) % 5]
            elif col_a == col_b:  # Same column: shift down
                encrypted_text += key_matrix[(row_a + 1) % 5][col_a]
                encrypted_text += key_matrix[(row_b + 1) % 5][col_b]
            else:  # Rectangle swap
                encrypted_text += key_matrix[row_a][col_b]
                encrypted_text += key_matrix[row_b][col_a]

        return encrypted_text

    @staticmethod
    def decrypt(text, key_matrix):
        decrypted_text = ""

        for i in range(0, len(text), 2):
            a, b = text[i], text[i + 1]
            row_a, col_a = playfair.find_position(key_matrix, a)
            row_b, col_b = playfair.find_position(key_matrix, b)

            if row_a == row_b:
                decrypted_text += key_matrix[row_a][(col_a - 1) % 5]
                decrypted_text += key_matrix[row_b][(col_b - 1) % 5]
            elif col_a == col_b:
                decrypted_text += key_matrix[(row_a - 1) % 5][col_a]
                decrypted_text += key_matrix[(row_b - 1) % 5][col_b]
            else:
                decrypted_text += key_matrix[row_a][col_b]
                decrypted_text += key_matrix[row_b][col_a]

        return decrypted_text

class multiplication:
    @staticmethod
    def about():
        return "The Caesar cipher but multiplication instead of addition. The decryption is different because just dividing letters will give you the same output for some inputs, so you have to use modular inverses. (https://www.dcode.fr/multiplicative-cipher)"

    @staticmethod
    def encrypt(text, key=randrange(1,26)):
        global lower_alphabet
        global upper_alphabet
        global alphabet

        verify_int_key(key)

        plaintext, punctuation_map, capitalization_map = process_text(text)

        ciphertext = ""

        for char in plaintext:
            char = char.upper()
            encrypted_char = chr(((ord(char) - ord('A')) * key) % 26 + ord('A'))
            ciphertext += encrypted_char

        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def decrypt(text, key=randrange(1,26)):
        global lower_alphabet
        global upper_alphabet
        global alphabet

        verify_int_key(key)

        text, punctuation_map, capitalization_map = process_text(text)

        plaintext = ""

        # Modular multiplicative inverse of the key
        key_inverse = pow(key, -1, 26)

        for char in text:
            char = char.upper()
            decrypted_char = chr(((ord(char) - ord('A')) * key_inverse) % 26 + ord('A'))
            plaintext += decrypted_char

        return reinflate(plaintext, punctuation_map, capitalization_map)

class multiplicative:
    @staticmethod
    def about():
        return multiplication.about()

    @staticmethod
    def encrypt(text, key=randrange(1,26)):
        return multiplication.encrypt(text)

    @staticmethod
    def decrypt(text, key=randrange(1,26)):
        return multiplication.decrypt(text)

class vigenere:
    @staticmethod
    def about():
        return "Vigenere cipher https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher"
    
    @staticmethod
    def encrypt(text, key):

        global lower_alphabet
        global upper_alphabet

        ciphertext=""
        passIndex=0

        text, punctuation_map, capitalization_map = process_text(text)

        for i in text:
            if i not in lower_alphabet and i not in upper_alphabet:
                ciphertext+=i
                continue

            value = lower_alphabet.index(i.lower())
            
            value = (value+lower_alphabet.index(key[passIndex].lower()))%26

            if i in lower_alphabet:
                ciphertext+=lower_alphabet[value]
            else:
                ciphertext+=upper_alphabet[value]

            if passIndex==len(key)-1:
                passIndex=0
            else:
                passIndex+=1

        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def decrypt(text, key):
 
        global lower_alphabet
        global upper_alphabet

        plaintext=""
        passIndex=0

        text, punctuation_map, capitalization_map = process_text(text)


        for i in text:
            if i not in lower_alphabet and i not in upper_alphabet:
                plaintext+=i
                continue

            value = lower_alphabet.index(i.lower())
            
            if i in lower_alphabet:
                value = (value-lower_alphabet.index(key[passIndex].lower()))
                if value<0: # If value is a negative number, wrap around the alphabet
                    value+=26
            else:
                value = (value-upper_alphabet.index(key[passIndex].lower()))
                if value<0: # If value is a negative number, wrap around the alphabet
                    value+=26

            if i in lower_alphabet:
                plaintext+=lower_alphabet[value]
            else:
                plaintext+=upper_alphabet[value]

            if passIndex==len(key)-1:
                passIndex=0
            else:
                passIndex+=1

        return reinflate(plaintext, punctuation_map, capitalization_map)

class atbash:

    @staticmethod
    def about():
        return "Atbash cipher, reverses text within the bounds of the alphabet (https://en.wikipedia.org/wiki/Atbash)"

    @staticmethod
    def atbash(text):
        global lower_alphabet
        global upper_alphabet
        ciphertext=""

        text, punctuation_map, capitalization_map = process_text(text)

        for i in text:
            if i in lower_alphabet:
                ciphertext+=lower_alphabet[25-lower_alphabet.index(i)]
            elif i in upper_alphabet:
                ciphertext+=upper_alphabet[25-upper_alphabet.index(i)]
            else:
                ciphertext+=i
        
        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def encrypt(text):
        return atbash(text)

    @staticmethod
    def decrypt(text):
        return encrypt(text)

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

class substitution:
    @staticmethod
    def about():
        return "Switch letters with other letters (https://en.wikipedia.org/wiki/Substitution_cipher)"

    @staticmethod
    def encrypt(plaintext, custom_alphabet):
        plaintext, punctuation_map, capitalization_map = process_text(plaintext)

        if len(custom_alphabet) != 26: raise Exception("Alphabet needs to be 26 characters long")

        key = dict(zip(string.ascii_lowercase, custom_alphabet.lower()))
        
        plaintext = plaintext.lower()
        ciphertext = []
        
        for char in plaintext:
            ciphertext.append(key[char])
                
        ciphertext = ''.join(ciphertext)
        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def decrypt(ciphertext, custom_alphabet):
        ciphertext, punctuation_map, capitalization_map = process_text(ciphertext)

        if len(custom_alphabet) != 26: raise Exception("Alphabet needs to be 26 characters long")

        key = dict(zip(string.ascii_lowercase, custom_alphabet.lower()))
        reversed_key = {v: k for k, v in key.items()}
        
        plaintext = []
        
        for char in ciphertext:
            plaintext.append(reversed_key[char])
            
        plaintext = ''.join(plaintext)
        return reinflate(plaintext, punctuation_map, capitalization_map)

class beaufort:
    @staticmethod
    def about():
        return "Built off of the Vigenere cipher (https://en.wikipedia.org/wiki/Beaufort_cipher)"

    @staticmethod
    def beaufort(text, key):
        verify_key_exists(key)

        text, punctuation_map, capitalization_map = process_text(text)

        global lower_alphabet
        key = key.lower()

        ciphertext = ""
        key_length = len(key)

        for i, char in enumerate(text):
            if char in lower_alphabet:
                key_char = key[i % key_length]
                char_index = lower_alphabet.index(char)
                key_index = lower_alphabet.index(key_char)
                encrypted_index = (key_index - char_index) % len(lower_alphabet)
                ciphertext += lower_alphabet[encrypted_index]

        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def encrypt(plaintext, key):
        return beaufort(plaintext, key)

    @staticmethod
    def decrypt(ciphertext, key):
        return beaufort(ciphertext, key)

class autokey:
    @staticmethod
    def about():
        return "Autokey cipher (https://en.wikipedia.org/wiki/Autokey_cipher)"

    @staticmethod
    def encrypt(plaintext, key):
        # Adapted from https://github.com/TheAlgorithms/Python/blob/master/ciphers/autokey.py
        # Autokey cipher

        verify_input(plaintext), verify_input(key)
        plaintext, punctuation_map, capitalization_map = process_text(plaintext)


        key += plaintext
        plaintext = plaintext.lower()
        key = key.lower()
        plaintext_iterator = 0
        key_iterator = 0
        ciphertext = ""
        while plaintext_iterator < len(plaintext):
            if (
                ord(plaintext[plaintext_iterator]) < 97
                or ord(plaintext[plaintext_iterator]) > 122
            ):
                ciphertext += plaintext[plaintext_iterator]
                plaintext_iterator += 1
            elif ord(key[key_iterator]) < 97 or ord(key[key_iterator]) > 122:
                key_iterator += 1
            else:
                ciphertext += chr(
                    (
                        (ord(plaintext[plaintext_iterator]) - 97 + ord(key[key_iterator]))
                        - 97
                    )
                    % 26
                    + 97
                )
                key_iterator += 1
                plaintext_iterator += 1

        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def decrypt(ciphertext, key):
        # Adapted from https://github.com/TheAlgorithms/Python/blob/master/ciphers/autokey.py
        # Autokey cipher

        verify_input(ciphertext), verify_input(key)
        ciphertext, punctuation_map, capitalization_map = process_text(ciphertext)

        key = key.lower()
        ciphertext_iterator = 0
        key_iterator = 0
        plaintext = ""
        while ciphertext_iterator < len(ciphertext):
            if (
                ord(ciphertext[ciphertext_iterator]) < 97
                or ord(ciphertext[ciphertext_iterator]) > 122
            ):
                plaintext += ciphertext[ciphertext_iterator]
            else:
                plaintext += chr(
                    (ord(ciphertext[ciphertext_iterator]) - ord(key[key_iterator])) % 26
                    + 97
                )
                key += chr(
                    (ord(ciphertext[ciphertext_iterator]) - ord(key[key_iterator])) % 26
                    + 97
                )
                key_iterator += 1
            ciphertext_iterator += 1

        return reinflate(plaintext, punctuation_map, capitalization_map)

class bifid:
    @staticmethod
    def about():
        return "Bifid cipher (https://en.wikipedia.org/wiki/Bifid_cipher)"

    @staticmethod
    def encrypt(plaintext, square):
        plaintext, punctuation_map, capitalization_map = process_text(plaintext)

        square = square.replace('j', 'i')
        square = [list(square[i:i+5]) for i in range(0, 25, 5)]

        def letter_to_numbers(letter, square):
            # Return the pair of numbers that represents the given letter in the polybius square.
            for row_idx, row in enumerate(square):
                if letter in row:
                    return row_idx + 1, row.index(letter) + 1
            raise ValueError(f"Letter {letter} not found in the square")

        def numbers_to_letter(row, col, square):
            # Return the letter corresponding to the position [row, col] in the polybius square.
            return square[row - 1][col - 1]

        rows, cols = [], []
        for letter in plaintext:
            row, col = letter_to_numbers(letter, square)
            rows.append(row)
            cols.append(col)

        merged = rows + cols
        ciphertext = ""

        for i in range(len(plaintext)):
            ciphertext += numbers_to_letter(merged[2 * i], merged[2 * i + 1], square)

        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def decrypt(ciphertext, square):
        ciphertext, punctuation_map, capitalization_map = process_text(ciphertext)

        square = square.replace('j', 'i')
        square = [list(square[i:i+5]) for i in range(0, 25, 5)]


        def letter_to_numbers(letter, square):
            # Return the pair of numbers that represents the given letter in the polybius square.
            for row_idx, row in enumerate(square):
                if letter in row:
                    return row_idx + 1, row.index(letter) + 1
            raise ValueError(f"Letter {letter} not found in the square")

        def numbers_to_letter(row, col, square):
            # Return the letter corresponding to the position [row, col] in the polybius square.
            return square[row - 1][col - 1]

        length = len(ciphertext)
        numbers = []
        for letter in ciphertext:
            row, col = letter_to_numbers(letter, square)
            numbers.extend([row, col])

        half_length = length
        rows = numbers[:half_length]
        cols = numbers[half_length:]

        ciphertext = ""
        for row, col in zip(rows, cols):
            ciphertext += numbers_to_letter(row, col, square)

        return reinflate(ciphertext, punctuation_map, capitalization_map)