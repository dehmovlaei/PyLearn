numFib = int(input("Enter the number of Fibo sequence digits to print\n"))
n0 = 0
n1 = 1
count = 0
if numFib <= 0:
    print("not valid sequence\n")
elif numFib == 1:
    print(n0)
else:
    while count < numFib:
        print(n0,",")
        nTmp = n0 + n1
        n0 = n1
        n1 = nTmp
        count += 1