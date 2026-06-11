rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1): # controls num of rows
    for space in range(1, (rows-i)+1): # 
        print(end="  ")
   
    while k!=(i+1-1):
        print("* ", end="")
        k += 1
    k = 0
    print()