def calculate_reading_time(str):
    if str == "":
        raise Exception("can't calcluate the reading time for empty text")
    words = str.split()
    return len(words)/200