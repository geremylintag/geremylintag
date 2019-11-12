def isWordGuessed(secretWord, lettersGuessed):
    for a in secretWord:
        if a not in lettersGuessed:
            return False
    return True