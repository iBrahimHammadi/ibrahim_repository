from Palindrome import palindrome
from unittest.mock import Mock
from unittest.mock import patch

pa = palindrome()


def test_palindrome_patch():
    with patch.object(palindrome,'reversed', return_value="eibohphobie"):
        assert pa.reversed("carac") == "eibohphobie"
        
        
def test_palindrome_patch_sideEffect():
    def reverse(s):
        return s == s[::-1]
    s = "7ama7"
    with patch.object(pa,'reversed',side_effect=reverse):
        assert pa.reversed(s) == True
   

def test_palindrome_mock_returnValue():
    pa.reversed= Mock(return_value=True)
    assert pa.reversed("ibrahim") == True
    
    
def test_palindrome_mock_sideEffect():
    def pa_mock(s):
        return s == s[::-1]
    s = "murdrum"
    pa.reversed = Mock(side_effect = pa_mock)
    assert pa.reversed(s) == True
