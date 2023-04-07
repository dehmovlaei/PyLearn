num = int(input("enter a number to cheak factorial: \n"))
index = fact = 1
while fact < num :
    index += 1
    fact *= index
if fact == num:
    print("is factorial")
else:
    print("is not")

