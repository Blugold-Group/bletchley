# Bletchley

Bletchley is a cryptography suite which provides tools for encryption, decryption, and cryptanalysis. It is aimed at classical ciphers

It can be used on the cli or in python code

**It is not stable, don't expect everything to work right just yet**

Bletchley has a number of tools to aid in cryptanalysis, including

1. Statistics
    - [x] Frequency analysis
    - [ ] Other things defined in lightbulb
    
2. Encryption and Decryption of the following ciphers
    - [x] Caesar
    - [x] Vigenere
    - [x] Rot13
    - [x] Enigma (through [pyenigma](https://pypi.org/project/pyenigma/))
    - [x] Atbash
    - [x] Playfair
    - [x] Affine
    - [x] Baconian
    - [x] Rail-Fence
    - [x] Substitution
    - [ ] Columnar Transposition
    - [x] Autokey
    - [x] Beaufort
    - [ ] Porta
    - [ ] Running Key
    - [ ] Homophonic Substitution
    - [ ] Four Square
    - [ ] Hill
    - [ ] ADFGVX
    - [ ] ADFGX
    - [x] Bifid
    - [ ] Trifid
    - [ ] Straddle Checkerboard 
    - [ ] Chaocipher

    Also, common encodings such as 
    - [ ] Base32
    - [ ] Base64
    - [ ] ASCII85

3. Attempted automated decryption of the following ciphers

    - [x] Caesar
    - [ ] Vigenere
    - [x] Rot13
    - [ ] Enigma (through [pyenigma](https://pypi.org/project/pyenigma/))
    - [x] Atbash
    - [ ] Playfair
    - [ ] Affine
    - [ ] Baconian
    - [ ] Rail-Fence
    - [ ] Substitution
    - [ ] Columnar Transposition
    - [ ] Autokey
    - [ ] Beaufort
    - [ ] Porta
    - [ ] Running Key
    - [ ] Homophonic Substitution
    - [ ] Four Square
    - [ ] Hill
    - [ ] ADFGVX
    - [ ] ADFGX
    - [ ] Bifid
    - [ ] Trifid
    - [ ] Straddle Checkerboard 
    - [ ] Chaocipher

4. A tool to determine which algorithm was used to make a hash, and a tool to search that hash in various online databases

And the crown jewel 

5. A dynamic tool using machine learning to guess what cipher was used to encrypt a ciphertext, codenamed lightbulb 

Works with the following ciphers
    - [ ] Vigenere
    - [ ] Atbash
    - [ ] Baconian


The power given by this repo is the ability to string various "huts" (tools) together, creating a dynamic solution finding tool. 

## Usage

```
python3 cli.py

OPTIONS

freq (frequency analysis)

-c,  --chart (Defaults to vbcol if not passed)
    c - count
    p - percentage
    vsbc - Verbose simple bar - count
    vbc - Verbose bar - count
    vsbca - Verbose simple bar - count, alphabetized
    vbca - Verbose bar - count, alphabetized
    vsbcar - Verbose simple bar - count, alphabetized reverse
    vbcar - Verbose bar - count, alphabetized reverse
    vsbcos - Verbose simple bar - count ordered smallest (to largest)
    vbcos - Verbose bar - count ordered smallest (to largest)
    vsbcol - Verbose simple bar - count ordered largest (to smallest)
    vbcol - Verbose bar - count ordered largest (to smallest)

run (try to automatically decrypt ciphertext)

-w, --wordlist
    large
    small
    small_specialized
    large_specialized
    dictionary

-v, --verbose
    - print the results of each test ran (true if passed, false if not)

encrypt (encrypt a text)

1 - Caesar cipher
2 - Vigenere cipher
3 - Rot13
4 - Atbash
5 - Playfair
6 - Baconian
7 - Affine
8 - Rail Fence
9 - Substitution
10 - Beaufort
11 - Autokey
12 - Bifid
13 - Trifid

decrypt (decrypt a text)

measure (measure some characteristic of a text)

classify (use lightbulb to guess what cipher was used to encrypt a text)

EXAMPLES

bletchley freq -t "hello world" -c vbcos
    - Return a bar chart of letter frequency of letter counts smallest to largest

bletchley freq -c p -t "hello world"
    - Return a list of letter frequency in the form of percentages

bletchley freq -t "hello world"
    - Return a bar chart of letter frequency of letter counts largest to smallest
```

### Description of word lists

The specialized word lists have been modified to perform better in this context

* small_quotes.txt - A file given by DOI:10.13140/RG.2.1.4386.4561 (10.8MB)
* large_quotes.txt - A file adapted from kaggle.com/datasets/manann/quotes-500k
* words_dictionary.json - A json-izes version of quotes.csv (6.8 MB)
* words.txt - A file of the top 20000 most commonly used english words (155.4 kB)
* dictionary.txt - The lowercase version of https://pypi.org/project/english-dictionary/ (1.2 MB)
* words_dictionary_specialized.txt - words_dictionary.json except all words with less than 4 characters and which aren't in dictionary.txt are removed (1.0 MB)

### Sources

Madadipouya, Kasra. (2016). CSV dataset of 76,000 quotes, suitable for quotes recommender systems or other analysis.. 10.13140/RG.2.1.4386.4561. 

english_dictionary (used for dictionary.txt) : https://pypi.org/project/english-dictionary/ Created by Daniel Delluomo 