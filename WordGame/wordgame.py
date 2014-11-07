import random
import string
import copy

HAND_SIZE = 7
# scrable letter: (value, distribution)
SCRABBLE_TILES = {
    'a': [1 , 9], 'b': [3 , 2], 'c': [3, 2], 'd': [2, 4], 'e': [1, 12],
    'f': [4 , 2], 'g': [2 , 3], 'h': [4, 2], 'i': [1, 9], 'j': [8, 1 ],
    'k': [5 , 1], 'l': [1 , 4], 'm': [3, 2], 'n': [1, 6], 'o': [1, 8 ],
    'p': [3 , 2], 'q': [10, 1], 'r': [1, 6], 's': [1, 4], 't': [1, 6 ],
    'u': [1 , 4], 'v': [4 , 2], 'w': [4, 2], 'x': [8, 1], 'y': [4, 2 ],
    'z': [10, 1]
    }

WORDLIST_FILENAME = "words.txt"

def load_words():
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

def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    score = 0
    for letter in word:
        score += SCRABBLE_TILES[letter][0]
    if len(word) == n:
        score += 50
    return score

def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """

    print("\nYour hand is")
    for letter in hand.keys():
        for j in range(hand[letter]):
            print (letter, end = ' ')   # prints all on the same line
    print()                             # print an empty line


def deal_hand():
    """
    Returns a random hand containing as many lowercase letters as the
    value of HAND_SIZE, with the same distribution as scrable

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    returns: dictionary (string -> int)
    """
    
    hand={}
    scrbbleTiles = copy.deepcopy(SCRABBLE_TILES)
    for tile in range (HAND_SIZE):
        tileNo = random.randrange(0,98 - tile)
        for letter in scrbbleTiles:
            tileNo -= scrbbleTiles[letter][1]
            if tileNo < 0:
                hand[letter] = hand.get(letter, 0) + 1
                scrbbleTiles[letter][1] -= 1
                break
    return hand
      
    


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """

    newHand = hand.copy()   # prevint mutation
    for letter in word:
        newHand[letter] -= 1
    return newHand
        

def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    wordDic = get_frequency_dict(word)
    inWordList = word in word_list
    inHand = not any(wordDic[letter] > hand.get(letter, 0)
                     for letter in wordDic.keys())
    return inWordList and inHand


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """

    scoreTot = 0
    while True:
        display_hand (hand)
        while True:
            userWord = input ("\nPlease input a word from your hand or '.' to stop. \n --> ")
            if is_valid_word(userWord, hand, word_list):
                break
            elif userWord == ".":
                print ("\nIn that hand you scored", scoreTot)
                return
            else:
                print ("\nThe word you input is ether not in your hand or not in the dictionary.\nPlease try again.\n")
        hand = update_hand(hand, userWord)
        score = get_word_score(userWord, HAND_SIZE) #update score
        scoreTot += score
        print ("\nThat word scored,", score)
        print ("Your score total is now,", scoreTot)
        sumHand = 0
        for x in hand: # check there are still letters in the hand
            sumHand += hand[x]
        if sumHand <= 0:
            break
        print ()
    print ("\nIn that hand you scored", scoreTot)
    
    
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    hand = deal_hand() # random init
    while True:
        cmd = input('\nEnter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand()
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print
        elif cmd == 'e':
            print ("Thanks for playing.\nGoodbye.")
            break
        else:
            print ("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

