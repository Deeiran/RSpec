# Exercise - One

#Calculate the extimate reading time

## 1.Discribe the Problem

As a user
So that I can manage my time
I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.

## 2.Disign the Method Signature

def calculate_reading_time(text):
    #Parameter:
        #text: a string contain words
    #Return:
        #float: reading time

## 3.Create Example as Tests. 

'''
given a text of 200 words string
it will return a reading time of 1
'''
calculate_reading_time(200words)
# => 1

'''
given a text of 400 words string
it will return a reading time of 1
'''
calculate_reading_time(400words)
# => 2

'''
given a text of 100 words string
it will return a reading time of 1
'''
calculate_reading_time(500words)
# => 0.5

'''
given a text of empty string
it will return a reading time of 1
'''
calculate_reading_time("")
# => exception message "can't calcluate the reading time for empty text"



## 4.Implement the Behaviour. 





# Exercise - TWO

#Check the Grammer

## 1.Discribe the Problem

As a user
So that I can improve my grammar
I want to verify that a text starts with a capital letter and ends with a suitable sentence-ending punctuation mark.

## 2.Disign the Method Signature

def check_grammer(text):
    #Parameter:
        #text: a string contain words
    #Return:
        #boolian: True/False

## 3.Create Example as Tests. 

'''
given a text start with capital letter and end with .
it will return true
'''
check_grammer(I love London.)
# => True

'''
given a text start with capital letter and end with?
it will return true
'''
check_grammer(Do I love London?)
# => True

'''
given a text start with capital letter and end with!
it will return true
'''
check_grammer(I love London!)
# => True

'''
given a text start with capital letter and end with,
it will return true
'''
check_grammer(I love London,)
# => False

'''
given a text start with lower letter and end with!
it will return true
'''
check_grammer(i love London!)
# => False

'''
given a text start with lower letter and end with,
it will return true
'''
check_grammer(i love London,)
# => False





## 4.Implement the Behaviour. 

# Challange - One

#Check the #TODO in a Text.

## 1.Discribe the Problem

As a user
So that I can keep track of my tasks
I want to check if a text includes the string #TODO.

## 2.Disign the Method Signature

def check_string(text):
    #Parameter:
        #text: a string contain words
    #Return:
        #boolian: True/False

## 3.Create Example as Tests. 

'''
string(#TODO) in the given text 
it will return True
'''
check_string("This is my #TODO list")
# => True


'''
Without string(#TODO) in the given text 
it will return False
'''
check_string("This is my todo list")
# => False

'''
empty sting in the given text 
it will raise an exception
'''
check_string("")
# => Message > "No Text given"





