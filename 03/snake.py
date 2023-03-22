j = 0
lenSnake = int(input("enter len of snake\n"))
for i in range(lenSnake):
    print("*", end = "")
    j += 1
    if j == lenSnake:
        break
    print("#", end = "")
    j += 1
    if j == lenSnake:
        break
    
    
