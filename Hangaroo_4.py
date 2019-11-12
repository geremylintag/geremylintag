def Hangaroo(secretWord):
    print("It's time for HANGAROOOO!!")
    print("This word consists of", len(secretWord), "letters.")
    mistakesMade = 0
    lettersGuessed = []
    
    while 6 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Nice! Great Job! GG!')
            break
        else:
            print('Remaining Guesses left:', 6 - mistakesMade)
            print('Available letters:', getAvailableLetters(lettersGuessed))
            letter = str(input('Enter a letter:')).lower()
            if (letter in secretWord and letter not in lettersGuessed):
            	lettersGuessed.append(letter)
            	print('Nice! Keep it Up!', getGuessedWord(secretWord, lettersGuessed))
            elif letter in lettersGuessed:
            	print("You have already used this letter: ", getGuessedWord(secretWord, lettersGuessed))
            elif letter not in secretWord:
            	print("That letter is not included: ", getGuessedWord(secretWord, lettersGuessed))
            	lettersGuessed.append(letter)
            	mistakesMade += 1
        if 6 - mistakesMade == 0:
            print('Game Over! The word is', secretWord)
            break
        else:
            continue