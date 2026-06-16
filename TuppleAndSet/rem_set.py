thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

print("Remove by discard")
thisset.discard("cherry")
print(thisset)

print("Remove by pop")
x = thisset.pop()   
print(x)
print(thisset)

print("Clear the set")
thisset.clear()
print(thisset)

print("Delete the set")
del thisset