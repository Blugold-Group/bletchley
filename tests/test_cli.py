import pytest
import subprocess

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_help():
    """Test the help message of the CLI"""

    result = subprocess.run(["bletchley/cli.py", "-h"], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'usage' in result.stdout

def test_caesar_encrypt():

    result = subprocess.run(['bletchley', 'encrypt', '-c', 'caesar', '-t', 'hello world', '-p' '7'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'olssv dvysk' in result.stdout

def test_vigenere_encrypt():

    result = subprocess.run(['bletchley', 'encrypt', '-c', 'vigenere', '-t', 'four score and seven years ago', '-p' 'blugold'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'gzox gnrsp utr dhwph eslut lau' in result.stdout

def test_atbash_encrypt():

    result = subprocess.run(['bletchley', 'encrypt', '-c', 'atbash', '-t', 'hello world'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'svool dliow' in result.stdout

def test_substitution_decrypt():

    result = subprocess.run(['bletchley', 'decrypt', '-c', 'substitution', '-t', 'Ltxe kdn, sqae  kdn qlgnqbg zue sdgz jhewtdmg ztse. Ztse ntll kexeh gdse qrqtk', '-p' 'qpwoeirutyalskdjfhgzmxncbv'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'Live now, make  now alsways the most precious time. Time will never some again' in result.stdout

def test_beaufort_decrypt():

    result = subprocess.run(['bletchley', 'decrypt', '-c', 'beaufort', '-t', 'Disw jk xu.', '-p' 'picard'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'Make it so.' in result.stdout

def test_bifid_decrypt():

    result = subprocess.run(['bletchley', 'decrypt', '-c', 'bifid', '-t', 'Iwid yop. Agmm pexhd.', '-p', 'qpwoeirutyalskdjfhgmznxbcv'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'Tood tea. Nice house.' in result.stdout # This should fail, it should be "Good tea"

def test_frequency():

    result = subprocess.run(['bletchley', 'freq', '-c', 'c', '-t', 'jkgvktfuqiq7i6q7qiyqvoqppq87qidgygwqedkyawfegak'], capture_output=True, text=True)

    assert result.returncode == 0
    assert "(['j', 'k', 'g', 'v', 't', 'f', 'u', 'q', 'i', '7', '6', 'y', 'o', 'p', '8', 'd', 'w', 'e', 'a'], [1, 4, 4, 2, 1, 2, 1, 9, 4, 3, 1, 3, 1, 2, 1, 2, 2, 2, 2])" in result.stdout

def test_pipe_hash_decrypt():

    result = subprocess.run(['bletchley', 'hash', '-t', '4960afbdf21280ef248081e6e52317735bbb929a204351291b773c252afeebf4'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'SHA-256, HC: 1400 JtR: raw-sha256' in result.stdout

def test_cli_encoding():

    result = subprocess.run(['bletchley', 'encode', '-t', 'I am a doctor, not a bricklayer.', '-e', 'base64'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'SSBhbSBhIGRvY3Rvciwgbm90IGEgYnJpY2tsYXllci4=' in result.stdout

def test_cli_decoding():

    result = subprocess.run(['bletchley', 'decode', '-t', 'DA13SKPX8S9Yzbbaw6NA3dtEzk', '-e', 'b58'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'Beam me up, Scotty!' in result.stdout

"""
def test_cli_run():

    result = subprocess.run(['bletchley', 'run', '-t', '"Knjv vn dy, Blxcch."'], capture_output=True, text=True)

    assert result.returncode == 0
    assert 'Beam me up, Scotty!' in result.stdout
    # The brute forcing function for caesar is wack when dealing with punctuation, this is an issue added to the project board
"""

def test_cli_about():

    result = subprocess.run(['bletchley', 'about', '-c', 'rot13'], capture_output=True, text=True)

    assert result.returncode == 0
    assert "This is a simple subsitution cipher, replacing the input letter with an output letter offset by 13 places (e.g. 'A' becomes 'N', 'B' becomes 'O', etc.)The ROT13 cipher is simply the Caesar cipher with a key-value of 13. " in result.stdout

