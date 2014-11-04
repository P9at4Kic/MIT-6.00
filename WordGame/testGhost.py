from ps5_ghost import *

def testDoYouLose(wordlist):
    wordFrags = (("apple", True), ("aahi", False), ("at", False), ("", False),
                 ("a", False), ("armt", True), ("ttt", True))
    i = 1
    for (wordFrag, exp) in wordFrags:
        test = doYouLose(wordFrag, wordlist) == exp
        print ("test", i, "is", test)
        i += 1

wordList = loadWords()
testDoYouLose(wordList)
