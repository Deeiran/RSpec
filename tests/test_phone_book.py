
from lib.phone_book import *
def test_initially_no_phone_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []


# """
# initally, there is no phone numbers
# """
# phone_book = PhoneBook()
# phone_book.list_numbers() = []

# # => []

from lib.phone_book import *
def test_diary_without_phone_numbers():
    phone_book = PhoneBook()
    assert phone_book.list_numbers() == []

# """
# When we add a diary entry without phone number init. there is no phone numbers to add to the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("My friend's number isn't relevant here")
# phone_book.list_numbers() = []

# # => []

def test_extractor_number_from_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jack's number 07545542926")
    assert phone_book.list_numbers() == ["07545542926"]

# """
# When we add a diary entry with phone number init. that phone number is added to the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("Jack's number 07545542926")
# phone_book.list_numbers() = ["07545542926]

# # => ["07545542926]


def test_multiple_diary_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jack's number 07545542926")
    phone_book.extract_numbers("Adam's number 07545542927")
    phone_book.extract_numbers("Joe's number 07545542925")
    phone_book.extract_numbers("James's number 07545542928")
    assert phone_book.list_numbers() == ["07545542926", "07545542927", "07545542925", "07545542928"]


# """
# When we add a multible diary entry with phone number init. that phone number is added to the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("Jack's number 07545542926")
# phone_book.extract_numbers("Adam's number 07545542927")
# phone_book.extract_numbers("Joe's number 07545542925")
# phone_book.extract_numbers("James's number 07545542928")
# phone_book.list_numbers() = ["07545542926 07545542926 07545542926 07545542926"]

# # => ["07545542926", "07545542926", "07545542926", "07545542926"]

def test_extract_multible_number_from_single_entry():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jack's number is 07545542926 and George's numbe is  07544442925")
    assert phone_book.list_numbers() == ["07545542926", "07544442925"]   


# """
# When we add a multible diary entry with multible phone numbers init. that phone number is added to the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("Jack's number is 07545542926" and George's numbe is  07544442925)

# phone_book.list_numbers() = ["07545542926", "07544442925"]

# # => ["07545542926", "07544442925"]


def test_number_not_started_with_zero():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jack's number is 777545542926")
    assert phone_book.list_numbers() == []
# """
# When we add diary entry with number not started with zero init. that phone number isn't added to the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("Jack's number is 777545542926")

# phone_book.list_numbers() = []


def test_more_than_eleven_number_():
    phone_book = PhoneBook()
    phone_book.extract_numbers("Jack's number is 0777545542926898")
    assert phone_book.list_numbers() == []
# """
# When we add diary entry with number more than 11 degits init. that phone number isn't added to the list
# """
# phone_book = PhoneBook()
# phone_book.extract_numbers("Jack's number is 777545542926")

# phone_book.list_numbers() = []