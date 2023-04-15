def khayamTriangle(row):
    triangle=[]
    for i in range(row):
        triangle.append([1]*(i+1))
        
    for i in range(2,row):  
        for j in range(1,i)  :
            triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j]
    return triangle  
      
row = int(input("Enter Number of rows: "))

finalList = khayamTriangle(row)
for i in finalList:
    print(i)