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
#from faker import Faker
import re 
import json
from random import randrange
from itertools import chain, cycle
import importlib.resources
#from numpy.random import choice

# Defining global alphabets/character sets/etc
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



class realEngine:
    """
    A class containing several methods that use wordlists consisting of samples of English words to determine whether an input contains a valid, English word.
    
    Attributes:
        data (list): A list of words loaded from specified corpus.
        corpus (str): The corpus type used for word validation.
    """
    def __init__(self, corpus="small_specialized"):
        """
        Initialized the realEngine with selceted wordlist corpus.

        Args:
            corpus (str): The corpus name (large, small, small_specialized, large_specialized, dictionary)

        """
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
        """
        Check whether the given string word exists in "real" words.

        Args:
            word (str): The word to validate.

        Returns:
            bool: True if word exists in corpus, otherwise False.
        """
        word=word.lower()

        if word in self.data:
            return True
        else:
            return False
    
    def plaintext_or_ciphertext(self, sentence, tolerance=0.51):
        """
        Determines if given sentence is likely English plaintext or ciphertext.

        Args:
            sentence (str): The input text.
            tolerance (float): Required percentage (as a decimal between 0 and 1) of words that must be "real" words. (Default 0.51)

        Returns:
            bool: True if text is more likely plaintext, otherwise False.
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
    """
    Validate input text for encryption or decryption.

    Args:
        text (str): The input string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the input string is empty.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    if not text:
        raise ValueError("text is empty")

def verify_key_exists(text):
    """
    Ensure the provided key exists and is a non-empty string.

    Args:
        key (str): The key to verify.

    Raises:
        TypeError: If the key is not a string.
        ValueError: If the kwy is empty.
    """
    if not isinstance(text, str):
        raise TypeError("Key must be a string")
    if not text:
        raise ValueError("You have to pass a key")

def verify_int_key(key):
    """
    Validate that a key is an integer.

    Args:
        key (int): The key to validate.

    Raises:
        TypeError: If the key is not an integer.
        ValueError: If the key is zero/invalid.
    """
    if not isinstance(key, int):
        raise TypeError("key must be an integer")
    if not key and key=="0":
        raise ValueError("key is empty")

class template:
    """
    This is a template that you may base future ciphers off of.
    Please provide a brief docstring (triple quotes) containing information about the given function/method/class, as well as its arguments and/or outputs.

    Methods:
        about() -> str: Provide information about the cipher.
        encrypt(plaintext, key) -> str: Encrypt plaintext, output ciphertext.
        decrypt(ciphertext, key) -> str: Decrypt cipher text, output plaintext.
        extra(thing, thing2) -> str: Do something else, probably an internal helper function.
    """
    @staticmethod
    def about():
        """Returns a brief description of the cipher, Wikipedia link, etc."""
        return "A little blurb about the cipher and how it works"

    @staticmethod
    def encrypt(plaintext, key):
        """Encrypts the given plaintext using the cipher."""
        return "Encrypt a text"

    @staticmethod
    def decrypt(ciphertext, key):
        """Decrypts the given ciphertext using the cipehr."""
        return "Decrypt a text"

    @staticmethod
    def extra(text, key):
        """Internal function used by the cipher."""
        return "Internal functions for use by the cipher"

class caesar:
    """
    A class implementing the Caesar cipher, a basic shift cipher.
    This class is also used for the ROT13 cipher.
    """
    @staticmethod
    def about(useRot13=False):
        """
        Returns information about the Caesar cipher or ROT13 cipher.

        Args:
            useRot13 (bool): If True, return details about the ROT13 variant.

        Returns:
            str: A description of the cipher (either ROT13 or Caesar as a whole).
        """
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
        """
        Encrypts text using the Caesar cipher.

        Args:
            text (str): Text to be encrypted.
            increment (int): The number of positions to shift. Defaults to a random value 1-26.

        Returns:
            str: The encrypted text.
        """
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
        """
        Decrypts text using the Caesar cipher.

        Args:
            text (str): The text to be decrypted.
            increment (int): Number of positions to shift. Defaults to random number 1-26.

        Returns:
            str: The decrypted text.
        """
        return caesar.encrypt(text, -increment)

class playfair:
    """
    A class implementing the Playfair cipher, a digraph substitution cipher.
    """
    @staticmethod
    def about():
        """
        Provides information about the Playfair cipher.

        Returns:
            str: A description of the Playfair cipher.
        """
        return ("Playfair cipher: https://en.wikipedia.org/wiki/Playfair_cipher\n"
                "This cipher encrypts text in letter pairs using a 5x5 key matrix, "
                "replacing 'J' with 'I' and inserting 'X' between duplicate letters or "
                "at the end of the message to maintain an even number of characters. "
                "Decryption preserves these alterations, which may lead to unexpected output.")

    @staticmethod
    def prepare_text(text):
        """
        Prepares text for encryption by making it uppercase, replacing 'J' with 'I', and inserting 'X' where needed.

        Args:
            text (str): The input text.

        Returns:
            str: The prepared text formatted for Playfair encryption.
        """
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
        """
        Generated the 5x5 key matrix used for Playfair encryption.

        Args:
            key (str): The keyword used for the key matrix.

        Returns:
            list: a 5x5 matrix as a 2 dimensional array list.
        """
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
        """
        Finds the row and column position of a letter in the key matrix.

        Args:
            matrix (list): The 5x5 Playfair matrix.
            char (str): The letter to locate.

        Returns:
            tuple: The row and column indices of the character in the matrix.
        """
        for row in range(5):
            for col in range(5):
                if matrix[row][col] == char:
                    return row, col
        return None

    @staticmethod
    def encrypt(text, key_matrix):
        """
        Encrypts text using the Playfair cipher.

        Args:
            text (str): The text to be encrypted.
            key_matrix (list): The 5x5 key matrix.

        Returns:
            str: The encrypted text.
        """
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
        """
        Decrypts text using the Playfair cipher.

        Args:
            text (str): The text to be decrypted.
            key_matrix (list): The 5x5 key matrix.

        Returns:
            str: The decrypted text.
        """
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
    """
    A class implementing the Multiplication cipher, a variation of the Caesar cipher.
    Instead of shifting letters by addition, it applies multiplication.
    """
    @staticmethod
    def about():
        """
        Provides information about the Multiplication cipher.

        Returns:
            str: A description of the Multiplication cipher.
        """
        return "The Caesar cipher but multiplication instead of addition. The decryption is different because just dividing letters will give you the same output for some inputs, so you have to use modular inverses. (https://www.dcode.fr/multiplicative-cipher)"

    @staticmethod
    def encrypt(text, key=randrange(1,26)):
        """
        Encrypts text using the Multiplication cipher.

        Args:
            text (str): The text to be encrypted.
            key (int): An integer between 1 and 26 for mmultiplication.

        Returns:
            str: The encrypted text.
        """
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
        """
        Decrypts text using the Multiplication cipher.

        Args:
            text (str): The text to be decrypted.
            key (int): The multiplication key used during encryption.

        Returns:
            str: The decrypted text.
        """
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
    """
    A wrapper class for the Multiplication cipher.
    The Multiplicative cipher is identical to the Multiplication cipher.
    """
    @staticmethod
    def about():
        """
        Provides information about the Multiplicative (Multiplication) cipher.

        Returns:
            str: A description of the Multiplicative cipher.
        """
        return multiplication.about()

    @staticmethod
    def encrypt(text, key=randrange(1,26)):
        """
        Encrypts text using the Multiplicative cipher.

        Args:
            text (str): The text to be encrypted.
            key (int): A key used for multiplcation.

        Returns:
            str: The encrypted text.
        """
        return multiplication.encrypt(text)

    @staticmethod
    def decrypt(text, key=randrange(1,26)):
        """
        Decrypts text using the Multiplicative cipher.

        Args:
            text (str): The text to be decrypted.
            key (int): The key used during encryption.

        Returns:
            str: The decrypted text.
        """
        return multiplication.decrypt(text)

class vigenere:
    """
    A class implementing the Vigenère cipher, a polyalphabetic substitution cipher.
    """
    @staticmethod
    def about():
        """
        Provides information about the Viegenère cipher.

        Returns:
            str: A description of the Vigeneère cipher.
        """
        return "Vigenère cipher https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher"
    
    @staticmethod
    def encrypt(text, key):
        """
        Encrypts text using the Vigenère cipher.

        Args:
            text (str): The text to be encrypted.
            key (str): The keyword used for encryption.

        Returns:
            str: The encrypted text.
        """
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
        """
        Decrypts text using the Vigenère cipher.

        Args:
            text (str): The text to be decrypted.
            key (str): The keyword used during encryption.

        Returns:
            str: The decrypted text.
        """
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
    """
    A class implementing the Atbash cipher, a simple monoalphabetic substutiion cipher
    that reverses the order of the alphabet.
    """
    @staticmethod
    def about():
        """
        Provides information about the Atbash cipher.

        Returns:
            str: A description of the Atbash cipher.
        """
        return "Atbash cipher, reverses text within the bounds of the alphabet (https://en.wikipedia.org/wiki/Atbash)"

    @staticmethod
    def atbash(text):
        """
        Encrypts or decrypts text using the Atbash cipher.
        Since Atbash is self-inverse cipher, encryption and decryption are identical processes.

        Args:
            text (str): The text to be encrypted/decrypted.

        Returns:
            str: The transformed text.
        """
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
        """
        Encrypts text using the Atbash cipher

        Args:
            text (str): The text to be encrypted.

        Returns:
            str: The encrypted text.
        """
        return atbash(text)

    @staticmethod
    def decrypt(text):
        """
        Decrypts text using the Atbash cipher.

        Args:
            text (str): The text to be decrypted.

        Returns:
            str: The decrypted text.
        """
        return atbash(text)
'''
class baconian:
    """
    A class implementing the Baconian cipher, a binary-based encoding scheme.
    """

    @staticmethod
    def about():
        """
        Provides information about the Baconian cipher.

        Returns:
            str: A description of the Baconian cipher.
        """
        return ("Baconian cipher encodes text into a binary-like form using two distinct characters "
                "(default 'a' and 'b'). See https://en.wikipedia.org/wiki/Bacon%27s_cipher for details.")
    
    @staticmethod
    def encrypt(text: str, l1="a", l2="b", style="old"):
        """
        Encrypts text using the Baconian cipher.

        Args:
            text (str): The text to be encrypted.
            l1 (str): The first character representing '0' in binary form.
            l2 (str): The second character representing '1' in binary form.
            style (str): Either "old" (where 'I' and 'J' share a code, and 'U' and 'V' share a code)
                         or "new" (where all letters have unique codes).

        Returns:
            str: The encrypted Baconian text.
        """
        global lower_alphabet
        encrypted = ""
        text = text.lower()

        for char in text:
            if char not in lower_alphabet:
                continue
            index = lower_alphabet.index(char)
            if style == "old":
                if index > 20:
                    index -= 2
                elif index > 8:
                    index -= 1
            binary = f"{index:05b}"  # Convert index to a 5-bit binary string
            bacon_text = "".join(l1 if bit == "0" else l2 for bit in binary)
            encrypted += bacon_text + " "

        return encrypted.strip()
'''

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

'''
class affine:
    """
    A class implementing the Affine cipher a monoalphabetic cipher
    using a linear functin to change each letter in the alphabet.
    """
    
    @staticmethod
    def about():
        """
        Provides information about the Affine cipher.

        Returns:
            str: A description of the Affine cipher.
        """
        return "The Affine cipher is a type of monoalphabetic substitution cipher that encrypts text using a mathematical function. (https://en.wikipedia.org/wiki/Affine_cipher)"
    
    @staticmethod
    def encrypt(plaintext, key1 = randrange(1, 25), key2 = randrange(1, 25)):
        """
        Encrypts text using the Affine cipher.

        Args:
            plaintext (str): The text to be encrypted.
            key1 (int): The first key used for multiplication (must be coprime to 26).
            key2 (int): The second key used for addition.

        Returns:
            str: The encrypted ciphertext.
        """
        global lower_alphabet, upper_alphabet
        ciphertext = ""

        plaintext, punctuation_map, capitalization_map = process_text(plaintext)

        for char in plaintext:
            if char.lower() in lower_alphabet:
                index = (key1 * lower_alphabet.index(char.lower()) + key2) % 26
                if char in lower_alphabet:
                    ciphertext += lower_alphabet[index]
                else:
                    ciphertext += upper_alphabet[index]
            else:
                ciphertext += char

        return reinflate(ciphertext, punctuation_map, capitalization_map)
    
    @staticmethod
    def decrypt(ciphertext, key1, key2):
        """
        Decrypts text using the Affine cipher.

        Args:
            ciphertext (str): The text to be decrypted.
            key1 (int): The first key used for multiplication (must be coprime to 26).
            key2 (int): The second key used for subtraction.

        Returns:
            str: The decrypted plaintext.

        Raises:
            ValueError: If key1 has no modular inverse under module 26.
        """
        global lower_alphabet, upper_alphabet
        plaintext = ""

        ciphertext, punctuation_map, capitalization_map = process_text(ciphertext)

        try:
            key1_inverse = pow(key1, -1, 26)
        except ValueError:
            raise ValueError("Key1 must be coprime to 26 (it needs a modular inverse).")
        
        for char in ciphertext:
            if char.lower() in lower_alphabet:
                index = (key1_inverse * (lower_alphabet.index(char.lower()) - key2)) % 26
                if char in lower_alphabet:
                    plaintext += lower_alphabet[index]
                else:
                    plaintext += upper_alphabet[index]
            else:
                plaintext += char

        return reinflate(plaintext, punctuation_map, capitalization_map)
    
class rail_fence:
    """
    A class implementing the Rail Fence cipher, a transposition cipher that rearranges text
    by writing it in a zigzag pattern across given number of rows.
    """

    @staticmethod
    def about():
        """
        Provides information about the Rail Fence cipher.

        Returns:
            str: A description of the Rail Fence cipher.
        """
        return "The Rail Fence cipher is a transposition cipher that writes plaintext in a zigzag pattern and reads it row by row. (https://en.wikipedia.org/wiki/Rail_fence_cipher)"
    
    @staticmethod
    def encrypt(plaintext, num_rails = randrange(2, 7)):
        """
        Encrypts text using the Rail Fence cipher.

        Args:
            plaintext (str): The text to be encrypted.
            num_rails (int): The number of rails (rows) used in the zigzag pattern.

        Returns:
            str: The encrypted ciphertext.

        Raises:
            ValueError: If num_rails is less than 2.
        """

        if num_rails < 2:
            raise ValueError("Rail Fence requires at least 2 rails.")
        
        plaintext, punctuation_map, capitalization_map = process_text(plaintext)

        rails = [[] for _ in range(num_rails)]
        rail, step = 0, 1

        for char in plaintext:
            rails[rail].append(char)
            rail += step
            if rail == num_rails - 1 or rail == 0:
                step = -step

        ciphertext = ''.join([''.join(rail) for rail in rails])
        return reinflate(ciphertext, punctuation_map, capitalization_map)
    
    @staticmethod
    def decrypt(ciphertext, num_rails):
        """
        Decrypts text using the Rail Fence cipher.

        Args:
            ciphertext (str): The text to be decrypted.
            num_rails (int): The number of rails (rows) used in encryption.

        Returns:
            str: The decrypted plaintext.

        Raises:
            ValueError: If num_rails is less than 2.
        """

        if num_rails < 2:
            raise ValueError("Rail Fence requires at least 2 rails.")
        
        ciphertext, punctuation_map, capitalization_map = process_text(ciphertext)

        rail_positions = [[] for _ in range(num_rails)]
        rail, step = 0, 1

        for _ in ciphertext:
            rail_positions[rail].append(None)
            rail += step
            if rail == num_rails - 1 or rail == 0:
                step = -step

        index = 0
        for rail in rail_positions:
            for i in range(len(rail)):
                rail[i] = ciphertext[index]
                index += 1
                
        plaintext = []
        rail, step = 0, 1
        for _ in ciphertext:
            plaintext.append(rail_positions[rail].pop(0))
            rail += step
            if rail == num_rails - 1 or rail == 0:
                step = -step

        return reinflate(''.join(plaintext), punctuation_map, capitalization_map)
'''
class substitution:
    """
    A class implementing a generic substitution cipher, where each letter is replaced
    in the plaintext with another letter according to a custom alphabet.
    """
    @staticmethod
    def about():
        """
        Provides information about the Substitution cipher.

        Returns:
            str: A description of the Substitution cipher.
        """
        return "A substitution is a cipher that replaces letters in the plaintext with different letters in the ciphertext according to a custom alphabet. (https://en.wikipedia.org/wiki/Substitution_cipher)"

    @staticmethod
    def encrypt(plaintext, custom_alphabet):
        """
        Encrypts text using a substitution cipher.

        Args:
            plaintext (str): The text to be encrypted.
            custom_alphabet (str): A 26-character custom alphabet to be used for substitution.

        Returns:
            str: The encrypted ciphertext.

        Raises:
            Exception: If the provided is alphabet is not exactly 26 characters in length.
        """
        plaintext, punctuation_map, capitalization_map = process_text(plaintext)

        if len(custom_alphabet) != 26: raise Exception("Alphabet must be exactly 26 characters long")

        key = dict(zip(string.ascii_lowercase, custom_alphabet.lower()))
        
        plaintext = plaintext.lower()
        ciphertext = []
        
        for char in plaintext:
            ciphertext.append(key[char])
                
        ciphertext = ''.join(ciphertext)
        return reinflate(ciphertext, punctuation_map, capitalization_map)

    @staticmethod
    def decrypt(ciphertext, custom_alphabet):
        """
        Decryptes text using a substitution cipher.

        Args:
            ciphertext (str): The text to be decrypted.
            custom_alphabet (str): The custom alphabet used during encryption.

        Returns:
            str: The decrypted plaintext.

        Raises:
            Exception: If the provided alphabet is not exactly 26 characters in length.
        """
        ciphertext, punctuation_map, capitalization_map = process_text(ciphertext)

        if len(custom_alphabet) != 26: raise Exception("Alphabet must be exactly 26 characters long")

        key = dict(zip(string.ascii_lowercase, custom_alphabet.lower()))
        reversed_key = {v: k for k, v in key.items()}
        
        plaintext = []
        
        for char in ciphertext:
            plaintext.append(reversed_key[char])
            
        plaintext = ''.join(plaintext)
        return reinflate(plaintext, punctuation_map, capitalization_map)

class beaufort:
    """
    A class implementing the Beaufort cipher, a polyalphabetic cipher
    similar to the Vigenère cipher but with different encryption formula.
    """
    @staticmethod
    def about():
        """
        Provides information about the Beaufort cipher.

        Returns:
            str: A description of the Beaufort cipher.
        """
        return "The Beaufort cipher is a variant of the Vigenère cipher (https://en.wikipedia.org/wiki/Beaufort_cipher)"

    @staticmethod
    def beaufort(text, key):
        """
        Encrypts and decrypts text using the Beaufort cipher.
        Note that Beaufort encryption and decryption are identical processes.

        Args:
            text (str): Either the plaintext or ciphertext to be encrypted or decrypted.
            key (str): The keyword used for encryption/decryption.
        
        Returns:
            str: The encrypted/decrypted plaintext/ciphertext.
        """
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
        """
        Encrypts plaintext using the Beaufort cipher.
        Note that Beaufort encryption and decryption are identical processes.

        Args:
            plaintext (str): The text to be encrypted.
            key (str): The keyword used for encryption.

        Returns:
            str: The encrypted ciphertext.
        """
        return beaufort(plaintext, key)

    @staticmethod
    def decrypt(ciphertext, key):
        """
        Decrypts ciphertext using the Beaufort cipher.
        Note that Beaufort encryption and decryption are identical processes.

        Args:
            ciphertext (str): The text to be decrypted.
            key (str): The keyword used during encryption.

        Returns:
            str: The decrypted plaintext.
        """
        return beaufort(ciphertext, key)

class autokey:
    """
    A class implemetning the Autokey cipher, a variation of the Vigenère cipher
    that appends part of the plaintext to the key (hence "autokey") to increase security.
    """
    @staticmethod
    def about():
        """
        Provides information about the Autokey cipher.

        Returns:
            str: A description of the Autokey cipher.
        """
        return "A polyalphabetic cipher based on Vigenère that extends the key using plaintext. (https://en.wikipedia.org/wiki/Autokey_cipher)"

    @staticmethod
    def encrypt(plaintext, key):
        """
        Encrypts text using the Autokey cipher.

        Args:
            plaintext (str): The text to be encrypted.
            key (str): The initial key used for encryption.

        Returns:
            str: The encrypted text.
        """
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
        """
        Decrypts text using the Autokey cipher

        Args:
            ciphertext (str): The text to be decrypted.
            key (str): The initial key used during encryption.
        """
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
    """
    A class implementing the Bifid cipher, a fractionated cipher that combines
    polybius squre encoding with transposition.
    """
    @staticmethod
    def about():
        """
        Provides information about the Bifid cipher.

        Returns:
            str: A description of the Bifid cipher.
        """
        return "Bifid cipher (https://en.wikipedia.org/wiki/Bifid_cipher)"

    @staticmethod
    def encrypt(plaintext, square):
        """
        Encrypts text using the Bifid cipher.

        Args:
            plaintext (str): The text to be encrypted.
            square (str): A Polybius square used for encryption.

        Returns:
            str: The encrypted text.
        """
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
        """
        Decrypts text using the Bifid cipher.

        Args:
            ciphertext (str): The text to be decrypted.
            square (str): The Polybius square used during encryption.

        Returns:
            str: The decrypted text.
        """
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

class nonsense:
    """
    A class implementing the Nonsense cipher, which simply provides
    nonsensical output based on statistical word lengths in the English language.
    """
    @staticmethod
    def about():
        """
        Provides information about the Nonsense cipher.

        Returns:
            str: A description of the Nonsense cipher.
        """
        return "A cipher which is just random letters in lengths according to statistical word lengths of the english language (https://github.com/berzerk0/NonsenseCipher/)"

    @staticmethod
    def encrypt(length):
        """
        Generates an output of pseudo-random characters based on a given length.

        Args:
            length (int): The length of nonsense to be returned.

        Returns:
            str: The nonsensical output of given length.
        """
        return nonsense(length)

    @staticmethod
    def decrypt(length):
        """
        Generates an output of pseudo-random characters based on a given length.

        Args:
            length (int): The length of nonsense to be returned.

        Returns:
            str: The nonsensical output of given length.
        """
        return nonsense(length)

    @staticmethod
    def wordLengthNonsense():
        """
        Defines statistical occurences of lengths of words in the English language.

        Returns:
            int: A randomly chosen word length based on given weights.
        """
        lengths = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        weights = [0.037264254570273500,0.175318842199986000,0.236406451194256000,0.189381282342557000,0.111243932166923000,0.078605655153973800,0.063440861055711100,0.040783187304009700,0.029444577786707800,0.017499282688117500,0.009119047190912850,0.006025419813131460,0.002855956737689010,0.001300152218663240,0.000620758184978121,0.000373705809092622,0.000136816980316337,0.000092253735299016,0.000057072226074815,0.000030490641327641]

        return random.choices(lengths, weights=weights, k=1)[0]

    @staticmethod
    def nonsense(length=random.randrange(1, 30)):
        """
        Generate a Nonsense cipher output of a given length
        length (int): The length of the output
        """
        result = ""

        length = int(length)

        for i in range(1, length + 1):
            # Use random.SystemRandom().choice to ensure randomness from the system
            addition = ''.join(random.SystemRandom().choice(string.ascii_uppercase) for _ in range(nonsense.wordLengthNonsense()))
            if i == 1:
                result = addition
            else:
                result = result + " " + addition
        return result