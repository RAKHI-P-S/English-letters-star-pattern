
for i in range(7):
    for j in range(7):
        if ((i == j and i < 4) or
            (i + j == 6 and i < 4) or
            (j == 3 and i >= 3)):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
