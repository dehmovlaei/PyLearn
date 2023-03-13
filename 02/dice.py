import random
while(input() != "end"):
    dice = random.randint(1, 6)
    print(dice)
    while dice == 6:
        dice = random.randint(1, 6)
        print(dice)