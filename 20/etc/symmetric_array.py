userList = input('enter a list of numbers seperated by a space: ').split(' ')
if len(userList) % 2 != 0:
    for i in range(0, (len(userList) // 2)):
        if userList[i] != userList[-1-i]:
            print('your array not symmetric')
            exit()
    print('your array are symmetric')
else:
    print('your array not symmetric')
