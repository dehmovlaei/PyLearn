import time
userInput = input("enter Time Like This HH:MM:SS To Convet into Second\n")
h, m, s, = userInput.split(':')
h = int(h)
m = int(m)
s = int(s)
m += h * 60
s +=  m * 60
print(userInput, "is", s,"Seconds")
