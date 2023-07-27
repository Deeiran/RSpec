def grammer_check(text):
    spc_cha = ('.','!','?')
    print (type(spc_cha))
    if text == "":
        raise Exception ("No Text Message Given")
    if (text[0].isupper()):
        for let in spc_cha:
            if let == text[-1]:
                return True
    return False    

