'''
Ваша програма має видати безперервну послідовність латинських літер в нижньому регістрі 
довжиною 1 000 000 символів. Послідовність має відповідати вимогам:
  Кожна літера з'являється не частіше 40 000 раз в послідовності;
  Кожна можлива послідовність з двох букв зявляється не частіше 2 000;
  Кожна можлива послідовність з трьох букв з'являється не частіше 100;
'''

import random


def createLetters():
    return dict.fromkeys ([a for a in 'abcdefghijklmnopqrstuvwxyz'], 0)


def getRandomLetter(lettersList, badLetters=set()):
    letter = random.choice(lettersList)
    for a in badLetters:
        if letter == a:
            lettersList.remove(letter)
            badLetters.remove(letter)
            return getRandomLetter(lettersList, badLetters)
    return letter


# The function adds only new combination of letters
def addKeysInDicts (twoLetters, threeLetters):
    global twoLettersDict
    global threeLettersDict
    
    if not twoLettersDict.__contains__(twoLetters):
        twoLettersDict [twoLetters] = 0
        
    if not threeLettersDict.__contains__(threeLetters):
        threeLettersDict [threeLetters] = 0


def addNextLetter():
    global lastTwoLetter
    
    global lettersDict
    global twoLettersDict
    global threeLettersDict
    
    global lettersForRandom
    
    global resultStr
    
    nextLetter = getRandomLetter(lettersForRandom)

    nextTwoLatters = lastTwoLetter[-1::] + nextLetter
    nextThreeLatters = lastTwoLetter + nextLetter

    if lettersDict.get(nextLetter) < 40000:
        
        addKeysInDicts(nextTwoLatters, nextThreeLatters)
        
        if twoLettersDict.get(nextTwoLatters) < 2000 and threeLettersDict.get(nextThreeLatters) < 100:
            lastTwoLetter = lastTwoLetter[1::] + nextLetter
            lettersDict[nextLetter] += 1
            twoLettersDict[nextTwoLatters] += 1
            threeLettersDict[nextThreeLatters] += 1
            resultFile.write(nextLetter)
        else:
            addNextLetter()
    else:
        lettersForRandom.remove(nextLetter)
        lettersDict.pop(nextLetter)


def start():
    global lastTwoLetter
    global resultFile
    
    lastTwoLetter = getRandomLetter(lettersForRandom) + getRandomLetter(lettersForRandom)
    resultFile.write(lastTwoLetter)
    i = 0
    while i < 1000000:
        addNextLetter()
        i += 1

# init global variables


# init verification dictionary
lettersDict = dict(createLetters())
twoLettersDict = dict()
threeLettersDict = dict()

# init other variables
lettersForRandom = list (lettersDict.keys())
lastTwoLetter = ''  

# init file to save result, because IDE don't want to write 1 m. letters
resultFile = open ('result.txt', 'a')

# START:
start()

resultFile.close()

# show verification info:
print(lettersDict)
print(twoLettersDict)
print(threeLettersDict)


