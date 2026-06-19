dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
allkey = dict1.keys() # keys() method will return a list of all the keys in the dictionary.
print (allkey)


x = dict1["model"] # use key to print Value
print (x)
x = dict1.get("model") #get() that will give you the same result

allvalues = dict1.values()
print (allvalues)
dict1["year"] = 2020 # Update year value 
dict1["newkey"] = "newvalue" # new value add
allitem = dict1.items() # print all values

print (dict1)

print (allitem)


