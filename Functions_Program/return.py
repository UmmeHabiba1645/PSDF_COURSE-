def my_function(x, y):
    return x + y

result = my_function(5, 3)
print(result)

print("Return diffrent data type")
def my_function():
    return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

print("Return tuple")
def my_function():
    return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)
