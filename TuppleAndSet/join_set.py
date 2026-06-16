print("By union() method")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

print("By | operator")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

print("Join multiple sets by union() method")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena", "Sarah"}

set4 = set1.union(set2, set3)
print(set4)

print("Join multiple sets by | operator")
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena", "Sarah"}
set4 = set1 | set2 | set3
print(set4)