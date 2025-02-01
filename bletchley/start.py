"""
The first things ran against a ciphertext

1. Cheap brute forcing
    - Caesar
    - Rot13
    - Substitution
    - Atbash

2. Machine Learning guess

3. Return suggestions or next steps for breaking guessed cipher

TODO:
    - Don't make finding one option end the script, try them all and return all results
    - Each brute forcing function creates a new realTest, make start.run() pass a shared engine, and have them only create their own if its not passed (a user might want to use the functions without start.run() or the cli)
    - Right now it just tries each cipher, but I want to get to the point of layering ciphers (ie caesar->vigenere->caesar)
    - Allow passing the plaintext detection tolerance (also from cli)

Rich Colors - https://rich.readthedocs.io/en/stable/appendix/colors.html

The tests work by passing the ciphertext to bruteforce.py for solving (including plaintext detection), unless the cipher doesn't take keys and is more of an encoding (IE Atbash). Then, the plaintext detection is handled in this file

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

def test_success(test, cipher, key, confidence):
    # The logging utility for a succeeded test
    console.print(f"[spring_green3]Text decrypted successfully! With a confidence of {"{:.3f}".format(confidence*100)}%, the plaintext is :[/spring_green3] {test}")
    console.print(f"[spring_green3]The ciphertext was encrypted with the [/spring_green3][bold]{cipher}[/bold] [spring_green3]cipher and used the key: [/spring_green3][bold dodger_blue3]{key}[/bold dodger_blue3]")

def test_success(test, cipher, key):
    # The logging utility for a succeeded test. This is for tests which can't handle or report confidence
    console.print(f"[spring_green3]Text decrypted successfully! The plaintext is :[/spring_green3] {test}")
    console.print(f"[spring_green3]The ciphertext was encrypted with the [/spring_green3][bold]{cipher}[/bold] [spring_green3]cipher and used the key: [/spring_green3][bold dodger_blue3]{key}[/bold dodger_blue3]")

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
        test_success(test[0], "caesar", test[1], test[2])
        return
    test_failed("Caesar Cipher", verbose)

    test=bruteforce.multiplication(ciphertext)
    if (test):
        test_success(test[0], "multiplicative", test[1], test[2])
        return
    test_failed("Multiplicative", verbose)

    test=bruteforce.vigenere(ciphertext, verbose)
    if (test):
        if len(test) > 2:
            test_success(test[0], "vigenere", test[1], test[2])
        else:
            test_success(test[0], "vigenere", test[1])

        return
    test_failed("Vigenere Cipher", verbose)

    if verbose: unavailable("railfence") # Automatic solving of the railfence cipher isn't supported yet
    """
    test=bruteforce.railfence(ciphertext)
    if (test):
        print("Railfence :", test[0], "key :", test[1])
        return
    test_failed("Rail Fence", verbose)
    """

    if verbose: unavailable("substitution") # Automatic solving of the substitution cipher isn't supported yet
    """
    test=bruteforce.substitution(ciphertext)
    if (test):
        print("Substitution :", test)
        return
    test_failed("Substitution Cipher", verbose)
    """

    test=bruteforce.atbash(ciphertext)
    if (test):
        print("Atbash :", test)
        return
    test_failed("Atbash Cipher", verbose)

    if verbose: unavailable("baconian")

    if verbose: unavailable("affine")

    if verbose: unavailable("beaufort")

    if verbose: unavailable("autokey")

    if verbose: unavailable("bifid")

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
            print("Enter decryption here")
            #print(ciphers.baconian(ciphertext))

    """
"""
ciphertexts=["Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.", "Zrc kewsg npaov hat beqfu ajcp zrc lidy xam.", "Twt byirz mvolc qsx yjxts dkpv twt wezn szk.", "baaba aabbb aabaa abbbb baabb abaaa aaaba abaab aaaab baaaa abbab babaa abbaa aabab abbab babab abaaa baabb ababb abbba baaab abbab baabb aabaa baaaa baaba aabbb aabaa ababa aaaaa babbb babba aaabb abbab aabba", "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.", "arIhtad  tete ?t  ahoehyjc fsorekr iuod edwgtiava hs teret w  th aoduhtn uao  otluwypstodon lu,n y eao  t hvgiiselaetl"]

for i in ciphertexts:
    run(i)

run("Aol xbpjr iyvdu mve qbtwz vcly aol shgf kvn.")
run("sdfkhvbhebfvihbev.")

"""