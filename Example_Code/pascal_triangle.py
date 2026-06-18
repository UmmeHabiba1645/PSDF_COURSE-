def pascal(n):
    row = [1]
    for i in range(n):
        print(row)
        row = [1] + [row[j] + row[j+1] for j in range(len(row)-1)] + [1]

pascal(5)