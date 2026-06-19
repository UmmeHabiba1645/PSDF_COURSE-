students = {
    "student1": {
        "name": "Arooj",
        "age": 20,
        "course": "AI"
    },
    "student2": {
        "name": "Ali",
        "age": 22,
        "course": "Python"
    }
}

## 1. copy()

print ("\n1. copy()")
students_copy = students.copy()
print (students_copy)

## 2. get()

print ("\n2. get()")
print (students.get("student1").get("name"))

## 3. key

print ("\n3. key()")
print (students.keys())

## 4. values()

print ("\n4. values()")
print (students.values())

## 5. items()

print ("\n5. items()")
print (students.items())

## 6. setdefalt()

print ("\n6. setdefalt()")
students.setdefault(
    "student3",
    {'name': 'Sara', 'age': 21, 'course': 'Data Science'}
)
print (students)

## 7. update()

print ("\n 7. update()")
students['student1'].update({"age": 26})
print (students)

## 8. pop 
print ("\n8. pop()")
removed_student = students.pop('student2')
print ("")
# ## 2. fromkeys()

# print("\n2. fromkeys()")
