rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):  # i=input(4) | range(start, stop, step) {start stope_at_0 step_i-=1} 
    for j in range(0, i):     # j = 0,1,2,4 (input)
        print("* " , end=" ")
    print()
