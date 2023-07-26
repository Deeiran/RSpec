def make_snippet(str):
    l_str = str.split(" ")
    count = len(l_str)
    if str == None:
        raise Exception("No Words Given")

    
    if count < 6:
        return str
    else: 
        first_five_words = ' '.join(l_str[:5])
        print(first_five_words)
        return first_five_words  + "..."
