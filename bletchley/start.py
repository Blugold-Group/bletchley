"""
The first things ran against a ciphertext

1. Cheap brute forcing
    - Caesar
    - Rot13
    - Substitution
    - Atbash

2. Machine Learning guess

3. Brute force the best guess

TODO:
    - Don't make finding one option end the script, try them all and return all results
    - Each brute forcing function creates a new realTest, make start.run() pass a shared engine, and have them only create their own if its not passed (a user might want to use the functions without start.run() or the cli)
    - Right now it just tries each cipher, but I want to get to the point of layering ciphers (ie caesar->vigenere->caesar)
    - When returning the solved plaintext, right now it just returns the planetext but I want to also return the key

Rich Colors - https://rich.readthedocs.io/en/stable/appendix/colors.html

"""

from rich.console import Console
from rich.text import Text
import shutil
import importlib.metadata

from . import ciphers
from . import bruteforce

console = Console()

def test_failed(test, verbose):
    # The logging utility for a failed test
    if verbose:
        console.print(f"[bold red]Test failed:  [/bold red][bold dodger_blue2]{test}[/bold dodger_blue2]")

def test_success(test, verbose):
    # The logging utility for a succeeded test
    if verbose:
        console.print(f"[spring_green3]Text decrypted successfully! :[/spring_green3] {test}")

def info(text):
    console.print(f"[deep_sky_blue1]Info:[/deep_sky_blue1]  {text}")

def unavailable(cipher):
    version = importlib.metadata.version("bletchley")
    console.print(f"Automatic solving for [bold cyan1]{cipher}[/bold cyan1] is currently [underline]unsupported[/underline]. You are running bletchley version [red][underline]{version}[/underline][/red]")

def run(ciphertext, wordlist="small_specialized", verbose=True):
    # Run tests to find the cipher a text was encrypted with

    console.print(f"[bold dodger_blue2]Starting decryption for ciphertext:[/bold dodger_blue2]  {ciphertext}")  # Make this look better

    realTest = ciphers.realEngine(wordlist)

    test=bruteforce.caesar(ciphertext)
    if (test):
        test_success(test, verbose)
        return
    test_failed("Caesar Cipher", verbose)

    test=bruteforce.railfence(ciphertext)
    if (test):
        print("Railfence :", test[0], "key :", test[1])
        return
    test_failed("Rail Fence", verbose)

    test=bruteforce.substitution(ciphertext)
    if (test):
        print("Substitution :", test)
        return
    test_failed("Substitution Cipher", verbose)

    test=ciphers.atbash(ciphertext)
    if (realTest.plaintext_or_ciphertext(test, 0.8)):
        print("Atbash :", test)
        return
    test_failed("Atbash Cipher", verbose)

    console.print(f"[bold red1]Automatic solving failed[/bold red1]")


    """
    info("Starting machine learning analysis")

    # ML Guess what the cipher is
    predicted=predict.predict_cipher(ciphertext)

    con=input("Found "+predicted+", do you want to run automatic decryption?  ")
    if con=="y":
        if predicted == "vigenere":
            bruteforce.vigenere(ciphertext)
        if predicted == "baconian":
            print("Enter decyrption here")
            #print(ciphers.baconian(ciphertext))

    """
