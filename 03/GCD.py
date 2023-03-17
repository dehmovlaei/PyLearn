n1, n2 = int(input("please enter FIRST digit\n")), int(input("please enter SECOND digit\n"))
n1Array, n2Array, GCD = [], [], []
for i in range(n1):
    if n1 % (i+1) == 0:
        n1Array.append(i+1)
print("First divisor: ", n1Array)
for i in range(n2):
    if n2 % (i+1) == 0:
        n2Array.append(i+1)
print("Second divisor: ", n2Array)
for i in range(len(n1Array)):
    if n1Array[i] in n2Array:
        GCD.append(n1Array[i])
print("CD :", GCD)
print("GCD :", GCD[len(GCD)-1])