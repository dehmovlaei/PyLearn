def mulTab (m, n):
    for i in range(m + 1):        
        for j in range(n + 1):            
            if i == 0:                
                if j == 0 :                    
                    print("X", "|", end="")                
                else:                    
                    print(j, "|", end="")            
            elif j == 0:                
                print(i, "|", end="")            
            else:                        
                print(i * j,"|", end="")        
        print()

m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

mulTab(m, n)
