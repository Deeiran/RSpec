def make_snippet(str):
    l_str = str.split(" ")
    count = len(l_str)
    if count < 5:
        return str
    else: 
        first_five_words = ' '.join(l_str[:5])
        print (type(first_five_words))
        return first_five_words  + "..."
    
make_snippet("a b c d e f")