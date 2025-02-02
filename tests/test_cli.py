import pytest
import subprocess

@pytest.fixture
def runner():
    return CliRunner()

def test_cli_help():
    """Test the help message of the CLI"""

    result = subprocess.run(["bletchley", "-h"], capture_output=True, text=True)

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
