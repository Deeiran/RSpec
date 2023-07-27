def check_string(text):
    if text == " ":
        raise Exception("No Text given")

    return True if '#TODO' in text else False