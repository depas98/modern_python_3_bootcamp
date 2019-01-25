total = 0

# def increment():
#     total += 1
#     return total
#
# print(increment()) # Error!

# global
total = 0


def increment():
    global total
    total += 1
    return total


print(increment())  # 1

#
# def say_hello():
#     instructor = 'Colt'
#     return f'Hello {instructor}'
#
# say_hello()
#
# print(instructor) # NameError

instructor = 'Colt'


def say_hello():
    return f'Hello {instructor}'


print(say_hello())  # 'Hello Colt'


# nonlocal
def outer():
    count = -99

    def inner():
        nonlocal count
        count += 1
        return count
    return inner()


print(outer())


# Default Parameters
def add(a, b):
    return a+b


def math(a, b, fn=add):
    return fn(a, b)


def subtract(a, b):
    return a-b


print(math(2, 2))  # 4
print(math(2, 2, subtract))  # 0


# def speak(animal ="dog"):
#     if animal == "dog":
#         return "woof"
#     elif animal == "pig":
#         return "oink"
#     elif animal == "duck":
#         return "quack"
#     elif animal == "cat":
#         return "meow"
#     else:
#         return "?"

# using dict
def speak(animal ="dog"):
    noises = {"dog": "woof",
              "pig": "oink",
              "duck": "quack",
              "cat": "meow"
              }

    noise = noises.get(animal)
    if noise:
        return noise
    return "?"


print(speak())
print(speak("pig"))
print(speak("duck"))
print(speak("cat"))
print(speak("dog"))
print(speak("banana"))
print(speak("unknown"))


def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"


print(say_hello.__doc__)

print(range.__doc__)


