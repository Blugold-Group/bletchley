"""
Provides utilities for encoding and decoding text using various standards.

This module supports multiple encodings, including common and obscure ones.
It also allows chaining multiple encodings in a sequence.

Each encoding follows a standardized representation:
    - Base64: 'base64', 'b64'
    - Base32: 'base32', 'b32'
    - Base58: 'base58', 'b58'
    - Base16 (Hexadecimal): 'base16', 'b16'
    - UTF-8: 'utf8', 'utf-8'
    - UTF-16: 'utf16', 'utf-16'
    - UTF-32: 'utf32', 'utf-32'
    - URL Encoding: 'url'
    - HTML Entity Encoding: 'html'
    - Shift_JIS: 'shiftjs', 'sjs'
    - ROT13: 'rot13'
    - Hexadecimal (Raw Bytes): 'hex', 'hexadecimal'
    - BZIP2: 'bzip2', 'bzip'
    - GZip: 'gzip'
    - Brotli: 'brotli', 'brot'

Supports encoding/decoding a string multiple times with the same or different encodings.
For example:
    - A string can be decoded with Base64 eight times.
    - A string can be decoded with Base64, then Base32, then Base32, then Base64.

 TODO: 
    - The function which runs a list of encodings formats the data into a string before passing to other encodings because it usually causes issues, someone has to research whether that would change things
"""

import base64
import base58
import urllib.parse
import html
import codecs
import bz2
import gzip
import brotli

# Base64 Encoding
def encode_base64(string):
    """
    Encodes a string using Base64 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base64-encoded string.
    """
    return base64.b64encode(string.encode('utf-8')).decode('utf-8')

# Base32 Encoding
def encode_base32(string):
    """
    Encodes a string using Base32 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base32-encoded string.
    """
    return base64.b32encode(string.encode('utf-8')).decode('utf-8')

# Base58 Encoding
def encode_base58(string):
    """
    Encodes a string using Base58 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base58-encoded string.
    """
    return base58.b58encode(string.encode('utf-8')).decode('utf-8')

# Base16 (Hexadecimal) Encoding
def encode_base16(string):
    """
    Encodes a string using Base16 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base16-encoded string.
    """
    return string.encode('utf-8').hex()

# UTF-8 Encoding
def encode_utf8(string):
    """
    Encodes a string using UTF-8 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The UTF-8-encoded string.
    """
    return string.encode('utf-8')

# URL Encoding (Percent Encoding)
def encode_url(string):
    """
    Encodes a string using URL encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The URL-encoded string.
    """
    return urllib.parse.quote(string)

# HTML Entity Encoding
def encode_html_entity(string):
    """
    Encodes a string using HTML Entity encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The HTML Entity-encoded string.
    """
    return html.escape(string)

# UTF-16 Encoding
def encode_utf16(string):
    """
    Encodes a string using UTF-16 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The UTF-16-encoded string.
    """
    return string.encode('utf-16')

# UTF-32 Encoding
def encode_utf32(string):
    """
    Encodes a string using UTF-32 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The UTF-32-encoded string.
    """
    return string.encode('utf-32')

# Shift_JIS Encoding
def encode_shift_jis(string):
    """
    Encodes a string using Shift JIS encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Shift JIS-encoded string.
    """
    return string.encode('shift_jis')

# Rot13 Encoding
def encode_rot13(string):
    """
    Encodes a string using ROT13 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The ROT13-encoded string.
    """
    return codecs.encode(string, 'rot_13')

# Hexadecimal Encoding (Raw bytes)
def encode_hex(string):
    """
    Encodes a string using Hex encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Hex-encoded string.
    """
    return string.encode('utf-8').hex()

# BZIP2 Encoding
def encode_bzip2(string):
    """
    Encodes a string using BZIP2 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The BZIP2-encoded string.
    """
    return bz2.compress(string.encode('utf-8'))

# Gzip Encoding
def encode_gzip(string):
    """
    Encodes a string using GZip encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The GZip-encoded string.
    """
    return gzip.compress(string.encode('utf-8'))

# Brotli Encoding
def encode_brotli(string):
    """
    Encodes a string using Brotli encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Brotli-encoded string.
    """
    return brotli.compress(string.encode('utf-8'))

# Decode Base64
def decode_base64(string):
    """
    Decodes a string using Base64 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base64-decoded string.
    """
    return base64.b64decode(string).decode('utf-8')

# Decode Base32
def decode_base32(string):
    """
    Decodes a string using Base32 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base32-decoded string.
    """
    return base64.b32decode(string).decode('utf-8')

# Decode Base58
def decode_base58(string):
    """
    Decodes a string using Base58 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base58-decoded string.
    """
    return base58.b58decode(string).decode('utf-8')

# Decode Base16 (Hexadecimal)
def decode_base16(string):
    """
    Decodes a string using Base16 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Base16-decoded string.
    """
    return bytes.fromhex(string).decode('utf-8')

# Decode UTF-8
def decode_utf8(string):
    """
    Decodes a string using UTF-8 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The UTF-8-decoded string.
    """
    return string.decode('utf-8')

# Decode URL Encoding (Percent Encoding)
def decode_url(string):
    """
    Decodes a string using URL encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The URL-decoded string.
    """
    return urllib.parse.unquote(string)

# Decode HTML Entity Encoding
def decode_html_entity(string):
    """
    Decodes a string using HTML Entity encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The HTML Entity-decoded string.
    """
    return html.unescape(string)

# Decode UTF-16
def decode_utf16(string):
    """
    Decodes a string using UTF-16 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The UTF-16-decoded string.
    """
    return string.decode('utf-16')

# Decode UTF-32
def decode_utf32(string):
    """
    Decodes a string using UTF-32 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The UTF-32-decoded string.
    """
    return string.decode('utf-32')

# Decode Shift_JIS (for Japanese text)
def decode_shift_jis(string):
    """
    Decodes a string using Shift JIS encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Shift JIS-decoded string.
    """
    return string.decode('shift_jis')

# Decode ROT13
def decode_rot13(string):
    """
    Decodes a string using ROT13 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The ROT13-decoded string.
    """
    return codecs.decode(string, 'rot_13')

# Decode Hexadecimal (Raw bytes)
def decode_hex(string):
    """
    Decodes a string using Hex encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Hex-decoded string.
    """
    return bytes.fromhex(string).decode('utf-8')

# Decode BZIP2
def decode_bzip2(string):
    """
    Decodes a string using BZIP2 encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The BZIP2-decoded string.
    """
    return bz2.decompress(string).decode('utf-8')

# Decode Gzip
def decode_gzip(string):
    """
    Decodes a string using GZip encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The GZip-decoded string.
    """
    return gzip.decompress(string).decode('utf-8')

# Decode Brotli
def decode_brotli(string):
    """
    Decodes a string using Brotli encoding.

    Args:
        string (str): The input string.

    Returns:
        str: The Brotli-decoded string.
    """
    return brotli.decompress(string).decode('utf-8')

encode_function_map = {
    'base64': encode_base64,
    'b64': encode_base64,
    'base32': encode_base32,
    'b32': encode_base32,
    'base58': encode_base58,
    'b58': encode_base58,
    'base16': encode_base16,
    'b16': encode_base16,
    'utf8': encode_utf8,
    'utf16': encode_utf16,
    'utf32': encode_utf32,
    'utf-8': encode_utf8,
    'utf-16': encode_utf16,
    'utf-32': encode_utf32,
    'url': encode_url,
    'html': encode_html_entity,
    'shiftjs': encode_shift_jis,
    'sjs': encode_shift_jis,
    'rot13': encode_rot13,
    'hex': encode_hex,
    'hexadecimal': encode_hex,
    'bzip': encode_bzip2,
    'bzip2': encode_bzip2,
    'gzip': encode_gzip,
    'brotli': encode_brotli,
    'brot': encode_brotli
}

decode_function_map = {
    'base64': decode_base64,
    'b64': decode_base64,
    'base32': decode_base32,
    'b32': decode_base32,
    'base58': decode_base58,
    'b58': decode_base58,
    'base16': decode_base16,
    'b16': decode_base16,
    'utf8': decode_utf8,
    'utf16': decode_utf16,
    'utf32': decode_utf32,
    'utf-8': decode_utf8,
    'utf-16': decode_utf16,
    'utf-32': decode_utf32,
    'url': decode_url,
    'html': decode_html_entity,
    'shiftjs': decode_shift_jis,
    'sjs': decode_shift_jis,
    'rot13': decode_rot13,
    'hex': decode_hex,
    'hexadecimal': decode_hex,
    'bzip': decode_bzip2,
    'bzip2': decode_bzip2,
    'gzip': decode_gzip,
    'brotli': decode_brotli,
    'brot': decode_brotli
}

def encode(text, encoding):
    """
    Encodes a string using one or more encoding methods.

    Args:
        text (str): The input string.
        encoding (str): The encoding method(s) (comma-separated).

    Raises:
        Exception: If an uknnown/invalid encoding is encountered.
    """
    # Encoding can have multiple encodings, in the form of ('base64, base32, base64, ascii')

    if "," in encoding:
        encoding = encoding.split(",")
    else:
        encoding = encoding.split()

    for code in encoding:
        code = code.strip()
        if code in encode_function_map:
            text = encode_function_map[code](str(text))

        else:
            print("Failed encoding:", code)
            raise Exception(f"Encoding not found.")

    print(text)
    
def decode(text, encoding):
    """
    Decodes a string using one or more decoding methods.

    Args:
        text (str): The encoded string.
        encoding (str): The decoding method(s) (comma-separated).

    Raises:
        Exception: If an unknown encoding is encountered.
    """
    # Decodings can have multiple encodings, in the form of ('base64, base32, base64, ascii')

    if "," in encoding:
        encoding = encoding.split(",")
    else:
        encoding = encoding.split()
    
    for code in encoding:
        code = code.strip()
        if code in decode_function_map:
            text = decode_function_map[code](str(text))

        else:
            print("Failed decoding:", code)
            raise Exception(f"Encoding not found.")

    print(text)
