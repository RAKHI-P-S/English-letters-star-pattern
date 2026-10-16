# letter M
for i in range(7):
    for j in range(11):
        if j==0 or j==10:
            print("*",end=" ")
        elif i==5 and j==5:
            print("*",end=" ")   
        elif i==j and i<=4:
            print("*",end=" ")    
        elif i+j==10 and i<=4:
            print("*",end=" ")     
        else:
            print(" ",end=" ")        
    print()

