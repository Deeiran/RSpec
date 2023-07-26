from lib.reading_time import *
import pytest 

def test_with_two_hundrad():
    text = " ".join(["word" for i in range(0, 200)])
    result = calculate_reading_time(text)
    assert result == 1.0

def test_with_four_hundrad():
    text = " ".join(["word" for i in range(0, 400)])
    result = calculate_reading_time(text)
    assert result == 2.0

def test_with_hundrad():
    text = " ".join(["word" for i in range(0, 100)])
    result = calculate_reading_time(text)
    assert result == 0.5

def test_with_empty():
    with pytest.raises(Exception) as e:
        calculate_reading_time("")
    error_message = str(e.value)
    assert error_message == "can't calcluate the reading time for empty text"


   
    

  
