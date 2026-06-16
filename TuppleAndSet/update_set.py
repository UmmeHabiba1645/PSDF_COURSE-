print("Update Set by one item")
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

print("Add elements from tropical set to thisset")
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

print("Add elements from a list to thisset")
mylist = ["kiwi", "watermelon"]
thisset.update(mylist)
print(thisset)

