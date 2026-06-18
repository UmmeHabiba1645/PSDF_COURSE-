def outer():
    def inner():
        return "Inner Function"

    return inner()

print(outer())