import random

# -----------------------------------
# Helper code

import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------


def doYouLose (wordFrag, wordList):
    """
    Returns True if the player loses and False if they do not
    wordFrag: string
    wordlist: list of lowercase strings
    """
    isWord = wordFrag in wordList
    isWordLong = len(wordFrag) > 3
    canBeWord = any(x.find(wordFrag) == 0 for x in wordList)
    return (isWord and isWordLong) or not canBeWord


def inputLetter (player):
    while True:
        try:
            letter = input ("Please input a letter.\n--> ")
            assert len(letter) == 1
            assert letter in string.ascii_letters
            letter = letter.lower()
            print ("Player", player, "says", letter, end="\n\n")
            return letter
        except:
            print ("You did not input a letter.\n")

def ghost (wordList):
    """Starts game of ghost"""
    wordFrag = ""
    print ("\nWelcome to ghost\n")
    while True:
        for player in ("one", "two"):
            print ("Curent word fragment is '", wordFrag, "'", sep="")
            print ("Player", player)
            letter = inputLetter(player)
            wordFrag += letter
            if doYouLose(wordFrag, wordList):
                print ("player", player, "loses")
                playAgain = input("If you would like to play again input y\n--> ")
                if playAgain.lower() != "y":
                    return
                ghost(wordList)
                    

 
if __name__ == '__main__':
    word_list = loadWords()
    ghost(word_list)        
    
    
