
from lib.class_grammarStats import *
import pytest 
"""
start with capital letter and end with ful stop
return true
"""

def test_start_capital_end_full_stop():
    grammar_check = GrammarStats()
    assert grammar_check.check("I love London.") == True

"""
start with capital letter and end with exclamation mark
return true
"""

def test_start_capital_end_exclamation_mark():
    grammar_check = GrammarStats()
    assert grammar_check.check("I love London!") == True

"""
start with capital letter and end with question mark
return true
"""

def test_start_capital_end_question_mark():
    grammar_check = GrammarStats()
    assert grammar_check.check("I love London?") == True

"""
start with capital letter and end with comma mark
return false
"""

def test_start_capital_end_comma_mark():
    grammar_check = GrammarStats()
    assert grammar_check.check("I love London,") == False

"""
start with lower letter and end with fullstop
return false
"""

def test_start_lower_end_full_stop():
    grammar_check = GrammarStats()
    assert grammar_check.check("i love London.") == False

"""
start with lower letter and end with comma
return false
"""

def test_start_lower_end_full_comma():
    grammar_check = GrammarStats()
    assert grammar_check.check("i love London,") == False

"""
no words given
raise error message - "No Text Message Given"
"""

def test_start_lower_end_full_comma():
    grammar_check = GrammarStats()
    with pytest.raises(Exception) as e:
        grammar_check.check("")
    assert str(e.value) == "No Text Message Given"

"""
run the test 4 times and correct 2
return 50
"""
def test_four_times_and_two_are_correct():
    grammar_check = GrammarStats()
    grammar_check.check("I love London.")
    grammar_check.check("I love London?")
    grammar_check.check("I love London,")
    grammar_check.check("i love London.")
    assert grammar_check.percentage_good() == 50

"""
run the test 3 times and correct 3
return 100
"""
def test_thre_times_and_all_are_correct():
    grammar_check = GrammarStats()
    grammar_check.check("I love London.")
    grammar_check.check("I love London?")
    grammar_check.check("I love London!")
    assert grammar_check.percentage_good() == 100

"""
run the test 3 times and correct 1
return 33.33
"""
def test_three_times_and_only_one_correct():
    grammar_check = GrammarStats()
    grammar_check.check("I love London.")
    grammar_check.check("i love London?")
    grammar_check.check("I love London,")
    assert grammar_check.percentage_good() == 33.33

"""
run the test 3 times and all wrong
return 0
"""
def test_three_times_and_all_wrong():
    grammar_check = GrammarStats()
    grammar_check.check("i love London.")
    grammar_check.check("i love London?")
    grammar_check.check("I love London,")
    assert grammar_check.percentage_good() == 0


"""
run the test 0 times and correct 0
return 0
"""
def test_ten_times_and_five_are_correct():
    grammar_check = GrammarStats()
    assert grammar_check.percentage_good() == 0


