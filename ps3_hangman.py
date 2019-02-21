# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return len(set(secretWord) & set(''.join(lettersGuessed))) == len(set(secretWord))


secretWord = 'apple' 
lettersGuessed = ['e', 'p', 'p', 'l', 'a', 's']
isWordGuessed(secretWord, lettersGuessed)


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = []
    for i in secretWord:
        if i in lettersGuessed:
            guessedWord.append(i)
        else:
            guessedWord.append('_')
    return ''.join(guessedWord)

secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'
print(getGuessedWord('z', ['z']))

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    result = set(string.ascii_lowercase) - set(''.join(lettersGuessed))
    return ''.join(sorted(result))

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # tell user the length of chosen word
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    lettersGuessed = []
    
    nguesses = 8
    while nguesses > 0:
        print('-----------')
        print('You have ' + str(nguesses) + ' guesses left.')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        guess = input('Please guess a letter:')
        guessInLowerCase = guess.lower()

        # check if letter is already guessed otherwise proceed 
        if guessInLowerCase in lettersGuessed:
            print("Oops! You've already guessed that letter:" + getGuessedWord(secretWord, lettersGuessed))
        else:
            lettersGuessed.append(guessInLowerCase)
            guessedWord = getGuessedWord(secretWord, lettersGuessed)
            if guessInLowerCase in set(secretWord):
                print('Good guess: ' + guessedWord)
            else:
                print('Oops! That letter is not in my word: ' + guessedWord)
                nguesses -= 1
        if isWordGuessed(secretWord, lettersGuessed):
            print('-----------')
            print('Congratulations, you won!')
            break
        if nguesses == 0:
            print('-----------')
            print('Sorry, you ran out of guesses. The word was '+ secretWord + '.')
    
hangman('z')




# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
