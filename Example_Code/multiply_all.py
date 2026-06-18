def multiply_list(lst):
    result = 1
    for i in lst:
        result *= i
        return result

print(multiply_list([8, 2, 3, -1, 7]))