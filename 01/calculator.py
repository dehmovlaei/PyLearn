import math
print("chose a Number For Witch Operation You Want To Do\n1.sum+\n2.sub-\n3.mul*\n4.div/\n5.pow^\n6.sqrt√\n7.sin\n8.cos\n9.tan\n10.cot\n11.fac!")
ope = int(input("youre Choice: "))
if (ope < 6):
    op1 = float(input("enter First Operand: "))
    op2 = float(input("enter Second Operand: "))
else:
    op3 = float(input("enter Operand: "))

if (ope == 1):
    result = op1 + op2
elif (ope == 2):
    result = op1 - op2
elif (ope == 3):
    result = op1 * op2
elif (ope == 4):
    result = op1 / op2
elif (ope == 5):
    result = op1 ** op2
elif (ope == 6):
    result = math.sqrt(op3)
elif (ope == 7):
    op3 = (op3*math.pi)/180
    result = math.sin(op3)
elif (ope == 8):
    op3 = (op3*math.pi)/180
    result = math.cos(op3)
elif (ope == 9):
    op3 = (op3*math.pi)/180
    result = math.tan(op3)
elif (ope == 10):
    op3 = (op3*math.pi)/180
    result = 1/math.tan(op3)
elif (ope == 11):
    result = math.factorial(int(op3))

print(result)