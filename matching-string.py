from string import *

targets = ['atgacatgcacaagtatgcat','atgaatgcatggatgtaaatgcag']
keys = ['a', 'atg', 'atgc', 'atgca']

def countSubStringMatch(target, key):
    count = 0
    aux = target.find(key)
    while aux != -1:
        count += 1
        aux = target.find(key, aux + 1)
    return count

def countSubStringMatchRecursive(target, key):
    targ = target.find(key)
    if targ == -1:
        return 0
    else:
        return countSubStringMatchRecursive(target[targ + 1:], key) + 1

def test1():
    for t in targets:
        for k in keys:
            print (countSubStringMatch(t, k), countSubStringMatchRecursive(t, k))

def subStringMatchExact(target,key):
    aux = [target.find(key)]
    while aux[-1] != -1:
        aux.append(target.find(key, aux[-1] + 1))
    return aux[:-1]

def test2():
    for t in targets:
        for k in keys:
            print(subStringMatchExact(t,k))

def constrainedMatchPair(firstMatch,secondMatch,length):
    aux = []
    for f in firstMatch:
            for s in secondMatch:
                if s - f - 1 - length == 0:
                    test = False 
                    for a in aux:
                        if a == f:
                            test = True
                    if test == False:
                        aux.append(f)
    return aux

def subStringMatchPartial(target,key):
    for x in range(len(key)):
        key1 = key[:x]
        key2 = key[x+1:]
        starts1 = subStringMatchExact(target, key1)
        starts2 = subStringMatchExact(target, key2)
        return constrainedMatchPair(starts1, starts2, len(key1))


def test3():
    for t in targets:
        for k in keys:
            print (subStringMatchPartial(t, k))
    
