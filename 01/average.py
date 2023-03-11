fName = input("please Insert Your First Name: ")
lName = input("please Insert Your Last Name: ")
one = int(input("score Test One: "))
two = int(input("score Test Two: "))
tree = int(input("score Test Tree: "))
avg = (one + two + tree)/3
if avg >= 17:
    print(fName,lName,"you Are Great With Average",avg)
elif  12<= avg < 17:
    print(fName, lName, "you Are Normal With Average", avg)
elif avg < 12:
    print(fName, lName, "you Are Fail With Average", avg)