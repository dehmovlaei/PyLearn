flag = True
total = 0
count =0
while(flag):
    score = input("please Enter Your Score: \nfor end type exit: ")
    if score == "exit" and count == 0:
        print("cannot Divide By Zero")
        flag = False
        break
    elif score == "exit":
        avg = total / count
        print("your Average Is: ",avg)
        flag = False
        break
    else:
        total += int(score)
        count += 1