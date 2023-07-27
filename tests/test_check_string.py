from lib.check_string import *
import pytest 

def test_check_string():
    result = check_string("This is my #TODO list")
    assert result == True


def test_without_string():
    result = check_string("This is my todo list")
    assert result == False


def test_with_empty_string():
    with pytest.raises(Exception) as e:
        check_string(" ")
    error_message = str(e.value)
    assert error_message == "No Text given"