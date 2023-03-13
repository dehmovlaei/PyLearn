import random
computerRand = (random.randint(1,10))
for i in range(5):
    userGuess = int(input("your Guess is: "))
    if userGuess == computerRand:
        print("😎congratulation you won after ",i+1,"guess")
        break
    elif userGuess < computerRand:
        print("⬆️guess Bigger One")
    elif userGuess > computerRand:
        print("⬇️guess smaller One")