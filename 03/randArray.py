import random
randArray = []
lenArray = int(input("how many random integer do you want to generate\n"))
for i in range(lenArray):
    randValue = random.randint(1, 10)
    if randValue in randArray:
        continue
    else:
        randArray.append(randValue)
print(randArray)

