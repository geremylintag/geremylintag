def getGuessedWord(secretWord, lettersGuessed):
    words = []
    for a in secretWord:
        if a in lettersGuessed:
            words.append(a)
        else:
            words.append("_")
    return "".join(words)