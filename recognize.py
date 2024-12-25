"""
This file provides modules to recognize what a ciphertext is encrypted with using static analysis

It does not use Machine Learning, but can accurate guesses as to what the cipher is based on cipher characteristics

It is designed to cut out possibilities for a cipher, and then pass on the text to the Machine Learning classification tool

"""

def guess(text):
    MD5=False
    SHA1=False
    RIPEMD128=False
    RIPEMD160=False
    RIPEMD256=False
    RIPEMD320=False
    Whirlpool=False
    SHA2224=False
    SHA2256=False
    SHA2384=False
    SHA2512=False
    SHA3224=False
    SHA3256=False
    SHA3384=False
    SHA3512=False
    SHAKE128=False
    SHAKE256=False
    Keccak224=False
    Keccak256=False
    Keccak384=False
    Keccak512=False

    if len(text)==32:
        MD5=True
        RIPEMD128=True
        return("MD5", "RIPEMD128")
    elif len(text)==40:
        RIPEMD160=True
        SHA1=True
        return("SHA1", "RIPEMD160")
    elif len(text)==56:
        SHA2224=True
        SHA3224=True
        Keccak224=True
        return("SHA2224", "SHA3224", "Keccak224")
    elif (len(text))==64:
        SHA3256=True
        Keccak256=True
        RIPEMD256=True
        return("SHA3256", "Keccak256", "RIPEMD256")
    elif (len(text))==80:
        RIPEMD320=True
        return("RIPEMD320")
    elif (len(text))==96:
        SHA3384=True
        Keccak256=True
        return("SHA3384", "Keccak256")
    elif (len(text))==128:
        SHA3512=True
        Keccak512=True
        return("SHA3512", "Keccak512")
    else:
        return(False)
