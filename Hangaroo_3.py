def getAvailableLetters(lettersGuessed):
    import string
    a = string.ascii_lowercase
    left = []
    for i in a:
        if i not in lettersGuessed:
            left.append(i)
    return "".join(left)