'''
string(#TODO) in the given text 
it will return True
check_string("This is my #TODO list")
# => True
'''
from lib.check_string import *
import pytest 

def test_check_string():
    result = check_string("This is my #TODO list")
    assert result == True