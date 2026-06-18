import string

def pangram(text):
    alphabet = set(string.ascii_lowercase)
    return alphabet <= set(text.lower())

print(pangram("The quick brown fox jumps over the lazy dog"))
print(pangram("Hello World"))