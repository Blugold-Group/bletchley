"""
Provides utilities to en/decode a string with a number of encoding standards

by design, the tool supports many encodings, including obscure encodings

The tools also support en/decoding a string multiple times with either the same of different standards

For example 'encodedstringhere' can be decoded by base64 eight times, or decoded with base64 then base32 then base32 then base64

"""

def encode(text, encoding):
    # Encoding can have multiple encodings, in the form of ('base64, base32, base64, ascii')
    print("Encode")

    for code in encoding.split():
        print(text.encode(encoding=code))

def decode(text, encoding):
    print("Decode")

def bruteforce(text):
    print("Brute fore decoding")

encode("test", "U8")