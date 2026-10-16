for i in range(7):
    for j in range(7):
        if (j == 0 or j == 6) and i < 6:
            print("*", end=" ")
        elif i == 6 and 0 < j < 6:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
