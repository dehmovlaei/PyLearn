def drawOval(iteration):
    m = iteration -1
    n = 1
    for i in range(0, iteration, 1):
        print(" " * m , "*" * n )
        m -= 1
        n += 2
    m += 2
    n -= 4
    for j in range(iteration - 1, 0, -1):
        print(" " * m, "*" * n)
        m += 1
        n -= 2

iteration = int(input("Enter the number of rows: "))

drawOval(iteration)