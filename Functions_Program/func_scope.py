print("inside function")
def myfunc():
    x = 300
    print(x)

myfunc()
def myfunc():
    x = 300
def myinnerfunc():
    print(x)
    myinnerfunc()

myfunc()

print("Global vs Local Scope")
x = 300

def myfunc():
    print("This is Global:", x)

myfunc()

print(x)

print("Overriding Global Scope")
x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)