def swp(square):
    if square == "⬛":
      square = "⬜"
    else:
      square = "⬛"
    return square
    
def chess(m, n):
    square = "⬛"
    for i in range(m):
        for j in range(n):
            print(square, end="")
            square = swp(square)      
        print()
        square = swp(square)

m = int(input())
n = int(input())
chess(m, n)