# letter A
# for i in range(7):
#     for j in range(5):
#         if i==0 or i==3 or j==0 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")        
#     print()

# # letter B
# for i in range(7):
#     for j in range(5):
#         if i==0 or i==3 or i==6 or j==0 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")        
#     print()

# # letter C
# for i in range(7):
#     for j in range(5):
#         if i==0  or i==6 or j==0 :
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")        
#     print()

# #  letter D
# for i in range(7):
#     for j in range(5):
#         if i==0 or i==6 or j==0 or j==4:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")        
#     print()

# # letter E
# for i in range(7):
#     for j in range(5):
#         if i==0 or i==3 or i==6 or j==0 :
#             print(" *",end=" ")
#         else:
#             print(" ", end=" ")    
#     print()        

# # letter F
# for i in range(7):
#     for j in range(5):
#         if i==0 or i==3  or j==0 :
#             print(" *",end=" ")
#         else:
#             print(" ", end=" ")    
#     print()        

# letter G
for i in range(7):
    for j in range(5):
        if i==0 or i==6  or j==0 :
            print("*",end=" ")
        elif i==3 and j>=2:
              print("*",end=" ")
        elif j==4 and i>=4:
             print("*",end=" ")
        else:
            print(" ", end=" ")    
    print()        