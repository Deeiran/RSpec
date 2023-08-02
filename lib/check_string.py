def check_string(text):
    if text == " ":
        raise Exception("No Text given")

    return '#TODO' in text