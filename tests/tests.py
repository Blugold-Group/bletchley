import pytest
from bletchley.cli import main
from bletchley import ciphers
from bletchley import bruteforce

def test_ciphers():
    assert ciphers.caesar.encrypt("hello world", 7) == "olssv dvysk"

def test_brute_force():
    assert bruteforce.caesar("olssv dvysk") == "hello world"

def test_cli_tool_run(monkeypatch, capsys):
    monkeypatch.setattr('sys.argv', ['bletchley', 'encrypt', '-c', 'caesar', '-t', 'hello world', '-p' '7'])
    
    from bletchley.cli import main
    main()
    
    captured = capsys.readouterr()
    assert "olssv dvysk" in captured.out
