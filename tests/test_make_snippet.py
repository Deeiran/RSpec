""" string is an argument in our function and we have only one argument
    need to findout the numbers of words in the sting 
    need to spilit the string to the list
    use len function to count the words
    conditional to check the the count words and if it is true index slices to get the first five words
    then we can add ... if that words are more than five
    we will design two test to assesrt if less than five words or equal,more than five words"""


from lib.make_snippet import *
import pytest 



def test_make_snippet_4words():        
    result = make_snippet("one two three four")
    assert result == "one two three four"

def test_make_snippet_6words():        
    result = make_snippet("one two three four five six")
    assert result == "one two three four five..."

def test_make_snippet_5words():        
    result = make_snippet("one two three four five")
    assert result == "one two three four five"

def test_make_snippet_0words():  
    with pytest.raises(Exception) as e:     
        make_snippet()
    error_message = str(e.value)
    assert error_message == "make_snippet() missing 1 required positional argument: 'str'"




