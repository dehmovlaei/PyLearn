import random
wordsBank = ["pink", "blue", "red", "green", "yello", "white", "black", "pourple", "orange" ]
x = random.randint(0, len(wordsBank)-1)
userMistakes, userCorrect  = 0, 0
trueChar, falseChar = [], []
word = random.choice(wordsBank)
while userMistakes < 6:
    endCounter = len(word)
    for i in range(endCounter):
        if word[i] in trueChar:
            print(word[i], end = "")
            endCounter -= 1
        else:
            print(" - ", end = "")
    if endCounter == 0:
        print("\nYOU WIN👌")
        break
    userGuess = input("\n guess some color:\n")
    userGuess = userGuess.lower()
    if len(userGuess) == 1:
        if userGuess in word:
            trueChar.append(userGuess)
        else:
            userMistakes += 1
            falseChar.append(userGuess)
    else:
        print("please enter only ONE char")
if userMistakes == 6:
    print("Game Over💀")