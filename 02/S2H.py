userInput = int(input("enter Time In Seconds\n"))
s = int(userInput % 60)
m = int(userInput / 60)
h = int(m / 60)
m = int(m % 60)
print(userInput, "Seconds Is:\n", h, ":", m, ":", s)