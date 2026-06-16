thisset = {"apple", "banana", "cherry"}
print(thisset)

print(type(thisset))
print("Duplicate items will be ignored:")
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

print("True and 1 are considered the same value:")
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

print("False and 0 are considered the same value:")
thisset = {"apple", "banana", "cherry", False, 0}
print(thisset)

