import pytest

class palindrome:
    def reversed(self,s):
        return s == s[::-1]
pa = palindrome()

def test_palindrome():
    assert pa.reversed("carac") == True
    assert pa.reversed("it is a boy yob a si ti") ==True
    assert pa.reversed("?.terret.?") == True
