rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i+1): # j=1,2.., go 1step further than i
        print(j, end=" ") 
    print()