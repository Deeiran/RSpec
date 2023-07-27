from lib.grammer_check import *
import pytest 

def test_start_capital_end_full_stop():
    result = grammer_check("I love London.")
    assert result == True

def test_start_capital_end_explanation_mark():
    result = grammer_check("I love London!")
    assert result == True

def test_start_capital_end_question_mark():
    result = grammer_check("I love London?")
    assert result == True

def test_start_capital_end_comma():
    result = grammer_check("I love London,")
    assert result == False

def test_start_lower_end_full_stop():
    result = grammer_check("i love London.")
    assert result == False

def test_start_lower_end_full_comma():
    result = grammer_check("i love London,")
    assert result == False

def test_start_lower_end_full_comma():
    with pytest.raises(Exception) as e:
        grammer_check("")
    error_message = str(e.value)
    assert error_message == "No Text Message Given"

