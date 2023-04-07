userArray, reversArray = [], []
print("enter your array elements\nfor end type exit")
while (True):
    elementArray = input()
    if elementArray == "exit":
        break
    else:
        userArray.append(elementArray)
for i in range (len(userArray), 0, -1):
    reversArray.append(userArray[i-1])
print(userArray, "\n", reversArray, sep="")