from caesar import encrypt as ceaser_encrypt
from vigenere import encrypt as vigenere_encrypt

def test_caesar():
    assert ceaser_encrypt('a', 13) == 'n'
    assert ceaser_encrypt('abcd', 13) == 'nopq'
    assert ceaser_encrypt('LaunchCode', 13) == 'YnhapuPbqr'
    assert ceaser_encrypt('LaunchCode', 1) == 'MbvodiDpef'
    assert ceaser_encrypt('Hello, World!', 5) == 'Mjqqt, Btwqi!'


def test_vigenere():
    assert vigenere_encrypt('The crow flies at midnight!', 'boom') == 'Uvs osck rmwse bh auebwsih!'