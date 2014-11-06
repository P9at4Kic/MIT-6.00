import random
import string
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
TIME_LIM = 30
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1,
    'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1,
    's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

WORDLIST_FILENAME = "words.txt"

def change_state ():
    global HAND_SIZE
    global TIME_LIM
    print("The current hand size is,", HAND_SIZE)
    print("The current time limit is,", TIME_LIM)
    while True:
        try:
            HAND_SIZE = int (input (
                "Please input a new value for the hand size:"))
            TIME_LIM = int (input (
                "Please input a new value for the time limit:"))
            assert HAND_SIZE > 0 and TIME_LIM > 0
            break
        except:
            print ("Please input positive intergers")
                                    

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
        score += SCRABBLE_LETTER_VALUES[letter]
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


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    
    hand={}
    num_vowels = n // 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
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


def decimal_place(num):
    """
    returns a string of a float to 2 decimal places
    num: float
    """
    num = str(num)
    decimal = num.find(".")
    return (num[:decimal+3])
    

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
    timeLeft = TIME_LIM
    while sum(hand.values()) > 0:
        display_hand (hand)
        sTime = time.time()
        print ("\nPlease input a word from your hand or '.' to stop. ")
        word = input (" --> ")
        eTime = time.time()
        tTime = eTime - sTime   # time taken to enter word
        timeLeft -= tTime       # time left to play hand
        if word == ".":
            break
        print ("You answered in", decimal_place(tTime), "seconds")
        if timeLeft < 0:
            print ("You have run out of time")
            break
        print ("You have", decimal_place(timeLeft), "seconds left.")
        if is_valid_word(word, hand, word_list):
            hand = update_hand(hand, word)
            score = get_word_score(word, HAND_SIZE) # get score
            score = score / tTime * 2               # adjust for time taken
            scoreTot += score
            print ("\nThat word scored,", decimal_place(score))
            print ("Your score total is now,", decimal_place(scoreTot))
        else:
            print ("\nThe word you input is ether not in your hand")
            print ("or not in the dictionary. Please try again.\n")
    print ("\nIn that hand you scored", decimal_place(scoreTot))
    
    
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

    while True:
        handExists = "hand" in locals()
        print ("\nEnter n to deal a new hand,")
        if handExists:
            print ("      r to replay the last hand,")
        print ("      i to reset the hand and time limit,")
        print ("      e to end game:")
        cmd = input("--> ")
        if cmd == "n":
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print
        elif cmd == "r" and handExists:
            play_hand(hand.copy(), word_list)
            print
        elif cmd == "e":
            print ("Thanks for playing.\nGoodbye.")
            break
        elif cmd == "i":
            change_state()
        else:
            print ("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

