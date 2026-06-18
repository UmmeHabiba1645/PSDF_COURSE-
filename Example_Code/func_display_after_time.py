print("Using Timer to display a message after 3 seconds")
from threading import Timer

def greet():
    print("Hello")

Timer(3, greet).start()