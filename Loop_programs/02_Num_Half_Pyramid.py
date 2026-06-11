rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):   # Auto updated value of j by for_loop
        print(j+1, end=" ")
    print()