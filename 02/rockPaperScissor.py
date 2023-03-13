import random
draw = 0
computerScore = 0
userScore = 0
flag = True
while(flag):
    computerChoice = random.choice(['Rock','Paper','Scissor'])
    userChoice = input("1-Rock | 2-Paper | 3-Scissor.......for End Type exit\n")
    if userChoice == "exit":
        flag = False
        print("🖥️computer Score is:",computerScore,"😎your Score is:",userScore,"Draw:",draw)
        break
    if userChoice == "1":
        print("your choice is: Rock")
        userChoiceStr = "Rock"
        print("computer choice is: ",computerChoice)
    elif userChoice == "2":
        print("your choice is: Paper")
        userChoiceStr = "Paper"
        print("computer choice is: ", computerChoice)
    elif userChoice == "3":
        print("your choice is: Scissor")
        userChoiceStr = "Scissor"
        print("computer choice is: ", computerChoice)
    else:
        userChoiceStr = "invalid"


    if userChoiceStr == computerChoice:
        draw += 1
        print("Draw")
    elif userChoiceStr == "Rock" and computerChoice == "Paper":
        computerScore +=1
        print("computer Win")
    elif userChoiceStr == "Rock" and computerChoice == "Scissor":
        userScore +=1
        print("you Win")
    elif userChoiceStr == "Paper" and computerChoice == "Scissor":
        computerScore +=1
        print("computer Win")
    elif userChoiceStr == "Paper" and computerChoice == "Rock":
        userScore +=1
        print("you Win")
    elif userChoiceStr == "Scissor" and computerChoice == "Rock":
        computerScore +=1
        print("computer Win")
    elif userChoiceStr == "Scissor" and computerChoice == "Paper":
        userScore +=1
        print("you Win")
    else:
        print("enter Correct Choice")