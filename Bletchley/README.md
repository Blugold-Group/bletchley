# Bletchley

A Cryptanalysis Suite 

Bletchley has a number of tools to aid in cryptanalysis, including

1. Frequency analysis
2. Automatic recognition and attempted decryption of various weak ciphers, including
    - [x] Ceaser
    - [ ] Vigenere
    - [ ] Rot13
    - [ ] Enigma
    - [ ] Atbash
    - [ ] Playfair
    - [ ] Rot13
    - [ ] Affine
    - [ ] Baconian
    - [ ] Rail-Fence
    - [ ] Substitution Cipher
    - [ ] Columnar Transposition Cipher
    - [ ] Autokey Cipher
    - [ ] Beaufort Cipher
    - [ ] Porta Cipher
    - [ ] Running Key Cipher
    - [ ] Homophonic Substitution Cipher
    - [ ] Four Square Cipher
    - [ ] Hill Cipher
    - [ ] ADFGVX Cipher
    - [ ] ADFGX Cipher
    - [ ] Bifid Cipher
    - [ ] Trifid Cipher
    - [ ] Straddle Checkerboard Cipher 

    Also, basic encodings such as 
    - [ ] Base32
    - [ ] Base64
    - [ ] ASCII85

    Can also recognize the following, but cannot decrypt them
    - [ ] MD5
    - [ ] SHA-1
    - [ ] RIPEMD-160
    - [ ] Whirlpool
    - [ ] SHA2-224
    - [ ] SHA2-256
    - [ ] SHA2-384
    - [ ] SHA2-512
    - [ ] SHA3-224
    - [ ] SHA3-256
    - [ ] SHA3-384
    - [ ] SHA3-512
    - [ ] SHAKE128
    - [ ] SHAKE256

3. A static tool which tests a ciphertext for the above ciphers
    - Uses hardcoded values with distinct characteristics of ciphertexts goven by these algorithms
4. Case transformers (upper to lowercase and vice versa)

And the crown jewel 
5. A dynamic tool built on machine learning which analyses ciphertext and gives best guesses as to what the cipher is and what steps can be taken to decrypt the ciphertext. Can also work with modern ciphers such as
    - AES-128
    - AES-256
    - ChaCha20

The power givin by this repo is the ability to string various "departments" (tools) together, creating a dynamic solution finding tool. 

Find what the plaintexts are likely to be, probably mostly quotes from GoodReads or something. 

Encrypt lots of plaintexts with various algorithms, and ML it to detect what cipher was used

## Description of wordlists

The specialized wordlists have been modified to perform better 

quotes.csv - A file given by DOI:10.13140/RG.2.1.4386.4561 (10.8MB)
words_dictionary.json - A json-izes version of quotes.csv (6.8 MB)
words.txt - A file of the top 20000 most commonly used elgish words (155.4 kB)
dictionary.txt - The lowercase verion of https://pypi.org/project/english-dictionary/ (1.2 MB)
words_dictionary_specialized.txt - words_dictionary.json except all words with less than 4 charcaters and which aren't in dictionary.txt are removed (1.0 MB)
words_specialized.txt - words.txt except all words with less than 4 charcaters and which aren't in dictionary.txt are removed (150.1 kB)



## Sources

Madadipouya, Kasra. (2016). CSV dataset of 76,000 quotes, suitable for quotes recommender systems or other analysis.. 10.13140/RG.2.1.4386.4561. 

english_dictionary (used for dictionary.txt) : https://pypi.org/project/english-dictionary/ Created by Daniel Delluomo 