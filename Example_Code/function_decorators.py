def bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

@bold
def text():
    return "Hello"

print(text())