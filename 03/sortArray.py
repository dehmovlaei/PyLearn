sortState = "IS sorted"
userArray = []
print("enter your array elements\nfor end type exit")
while (True):
    elementArray = input()
    if elementArray == "exit":
        break
    else:
        userArray.append(int(elementArray))
for i in range(len(userArray)-1):
    if userArray[i] < userArray[i+1]:
        continue
    else:
        sortState = "IS NOT sorted"
        break
print("you enter this array: ", userArray, sortState)

