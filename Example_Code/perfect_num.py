def perfect_number(n):
    total = sum(i for i in range(1, n) if n % i == 0)
    return total == n

print(perfect_number(28))
print(perfect_number(11))