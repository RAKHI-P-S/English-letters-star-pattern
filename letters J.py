for i in range(7):
    for j in range(5):
        if i==0 or j==2  :
             print("*", end=" ")

        elif i==0 and j==2:
            print("*", end=" ")

        elif i==6 and j<=2:
            print("*", end=" ")

        elif j==0 and i>=5:
            print("*", end=" ")
        else:
            print(" ",end=" ")    
    print()        