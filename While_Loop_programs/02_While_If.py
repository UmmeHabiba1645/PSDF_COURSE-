i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
x = 0
while x < 6:
  x += 1
  if x == 3:
    continue
  print(x)

y = 1
while y < 6:
  print(y)
  y += 1
else:
  print("y is no longer less than 6")