hight = 18
vidght = 110

for row in range(hight, 0, -1):
    for column in range(vidght, 0, -1):
        if row == 1 or row == 2 or row == 17  or row == 18:
            print ("*", end="")
        elif column == 85:
            print (" ", end="")
        elif column <= 85:
            print(" ", end="")
        else:
            print ("*", end="")
        
    print ("**")
    
    
# for i in range(rows, 1, -1):
#     for space in range(0, rows-i):
#         print("  ", end="")
#     for j in range(i, 2*i-1):
#         print("* ", end="")
#     for j in range(1, i-1):
#         print("* ", end="")
#     print()