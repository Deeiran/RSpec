from lib.diaryentry import *
import pytest 
import math


"""
Given an empty title and contents
raises an error
"""
def test_empty_title_and_contents():
    with pytest.raises(Exception) as e:
        DiaryEntry("","")
    error_message = str(e.value)
    assert error_message == "Diary entries must have a title or contents"


"""
Given a title and contents and return the formatted way 
"""
def formated_title_contents():
    diaryentry = DiaryEntry("My Title","some contents")
    result = diaryentry.format()
    assert result == "My Title: some contents"

'''
given a title and a contentes.
count the world in the title and contents
'''

def test_counting_words_in_both():
    diaryentry = DiaryEntry("My Title", "some contents")
    result = diaryentry.count_words()
    assert result == 4
"""
given a wpm of 2
and text with 2 words
#reading time should retrun 1 min
"""
def test_reading_time_with_two_wpm_and_two_words():
    diaryentry = DiaryEntry("My Title","some contents")
    result = diaryentry.reading_time(2)
    assert result == 1
"""
given a wpm of 2
and text with 4 words
#reading time should retrun 2 min
"""

def test_reading_time_with_two_wpm_and_four_words():
    diaryentry = DiaryEntry("My Title","some contents one two")
    result = diaryentry.reading_time(2)
    assert result == 2

"""
given a wpm of 2
and text with 3 words
#reading time should retrun 2 min
"""

def test_reading_time_with_two_wpm_and_three_words():
    diaryentry = DiaryEntry("My Title","some contents one")
    result = diaryentry.reading_time(2)
    assert result == 2

"""
given a wpm of 0
and text with 3 words
#reading time should raise error message
"""

def test_reading_time_with_two_wpm_and_zero_words():
    diaryentry = DiaryEntry("My Title","some contents one")
    with pytest.raises(Exception) as e:
        diaryentry.reading_time(0)
    assert str(e.value) == "cannot calculate the time with zero words"


"""
given words 6
given a wpm of 2
and givin minutes 1

#return chunk = 2 words.
"""
def test_given_six_words_two_wpm_two_min():
    diaryentry = DiaryEntry("My Title","some contents one two three four")
    result = diaryentry.reading_chunk(2,1)
    assert result == "some contents"

"""
given words 6
given a wpm of 2
and givin minutes 2

#return chunk = 4 words.
"""
def test_given_six_words_two_wpm_two_min():
    diaryentry = DiaryEntry("My Title","some contents one two three four")
    result = diaryentry.reading_chunk(2,2)
    assert result == "some contents one two"

"""
given content words 6
given a wpm of 2
and givin minutes 1

#first time rading chunk return 2 words second time next two words
"""
def test_given_six_words_two_wpm_repeated():
    diaryentry = DiaryEntry("My Title","some contents one two three four")
    assert diaryentry.reading_chunk(2,1) == "some contents"
    assert diaryentry.reading_chunk(2,1) == "one two"
"""
given content words 6
given a wpm of 2
and givin minutes 1

#first time rading chunk return 2 words second time next two words
"""
def test_given_six_words_two_wpm_repeated_again():
    diaryentry = DiaryEntry("My Title","some contents one two three four")
    assert diaryentry.reading_chunk(2,1) == "some contents"
    assert diaryentry.reading_chunk(2,1) == "one two"
    assert diaryentry.reading_chunk(2,2) == "three four"
    assert diaryentry.reading_chunk(2,1) == "some contents"