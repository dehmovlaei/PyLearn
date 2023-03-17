n1, n2 = int(input("please enter FIRST digit\n")), int(input("please enter SECOND digit\n"))
for i in range (max(n1, n2), (n1*n2) + 1):
    if i % n1 == i % n2 == 0:
        LCM = i
        break
print("LCM is", LCM)