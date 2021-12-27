# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"
lettersGuessed = []



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
    truth = []
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            truth.append('here')
            if len(truth) == len(secretWord):   
                return True
        else:
            return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    truth = []
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            truth.append(secretWord[i])
        else:
            truth.append('_')
    truth = ''.join(truth)
    return truth



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    l2 = lettersGuessed
    l1 = string.ascii_lowercase
    return ''.join([x for x in l1 if x not in l2])
    

def hangman(secretWord):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' +str(len(secretWord))+ ' letters long.')
    print('-------------')
    lettersGuessed = []
    def getInput(secretWord, lettersGuessed):
        number = 8
        for i in range(26):
            print('You have ' + str(number) + ' guesses left.')
            print('Avaliable letters: '+ str(getAvailableLetters(lettersGuessed)))
            user = input('Please guess a letter: ')
            lettersGuessed.append(user)
            if (lettersGuessed[i] in secretWord) and (lettersGuessed[i] not in str(lettersGuessed[0:len(lettersGuessed)-1])):
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            if (lettersGuessed[i] not in secretWord) and (lettersGuessed[i] not in str(lettersGuessed[0:len(lettersGuessed)-1])):
                print("Oops! That letter is not in my word: " + str(getGuessedWord(secretWord, lettersGuessed)))
                print('-------------')
                number -=1
            if lettersGuessed[i] in lettersGuessed[0:len(lettersGuessed)-1]:
                print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
                print('-------------')
            if getGuessedWord(secretWord, lettersGuessed) == secretWord:
                print('-------------')
                print('Congratulations, you won!')
                break
            if number == 0:
                print('Sorry, you ran out of guesses. The word was ' + str(secretWord))
                break
        return lettersGuessed
    getInput(secretWord, lettersGuessed)

secretWord = chooseWord(wordlist)
isWordGuessed(secretWord, lettersGuessed)
getGuessedWord(secretWord, lettersGuessed)
getAvailableLetters(lettersGuessed)
chooseWord(wordlist)
hangman(secretWord)



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


# hangman(secretWord)
