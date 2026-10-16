
for i in range(7):
    for j in range(13):
        if (j == 0 or j == 12 or
            (i >= 3 and
             (j == i or j == 12-i))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
