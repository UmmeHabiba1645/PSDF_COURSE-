dict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict.pop("model") # Remove selected item 
dict.popitem() # remove last item
del dict["model"]
# del thisdict # dell complete list 
# dict.clear() # clear complete list

print(dict)