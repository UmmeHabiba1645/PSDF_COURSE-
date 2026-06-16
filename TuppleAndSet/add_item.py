print("Update By Convert into a list, add item, and convert back into a tuple")
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

print("Update tuple by adding a tuple")
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)