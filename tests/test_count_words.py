""" This function is for count_ words and will take only one arguments:str 
    return the words in that string
    split in to your list using split method and using the len funtion to count the words
    expeceted output:int """

from lib.count_words import *
import pytest 

def test_count_words_in_the_str():
    result = count_words("Hey") 
    assert result == 1

def test_count_words_zero():
    result = count_words("") 
    assert result == 0