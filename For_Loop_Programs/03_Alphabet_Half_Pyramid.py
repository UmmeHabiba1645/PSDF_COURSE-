rows = int(input("Enter number of rows: "))

ascii_value = 71

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value) # char() converts a number (ASCII / Unicode value) into a character
        print(alphabet, end=" ")
        ascii_value += 1     # ascii_value = ascii_value + 1
    print()