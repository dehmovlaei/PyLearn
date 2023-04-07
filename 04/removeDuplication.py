userArray, removeArray = [], []
print("enter your array elements\nfor end type exit")
while (True):
    elementArray = input()
    if elementArray == "exit":
        break
    else:
        userArray.append(elementArray)
for i in userArray:
    if i not in removeArray:
        removeArray.append(i)
print(userArray, "\n", removeArray, sep="")

