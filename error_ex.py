def colorize(text, color):
    colors = ("cyan", "yellow", "blue", "green", "magenta")
    if type(text) is not str:
        raise TypeError("text must be instance of str")
    if type(color) is not str:
        raise TypeError("color must be instance of str")
    if color not in colors:
        # raise Exception
        raise ValueError(f"color is invalid needs to be on eof the following: {colors}")
    print(f"Printed {text} in {color}")


# colorize("hello", "red")
# colorize(34, "red")

# try:
#     foobar
# except:
#     print("Problem!")
#
# print("after the try")

d = {"name": "Ricky"}
# d["city"]


def get(d, key):
    try:
        return d[key]
    except KeyError:
        return None


print(get(d, "name"))
print(get(d, "city"))

# try:
#     num = int(input("Enter a numer: "))
# except ValueError:
#     print("That's not a number")
# else:
#     print("I'm in the else")
# finally:
#     print("always runs")


def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        return("Please do not divide by zero")
        # print(err)
    except TypeError as err:
        return("a and b must be ints or floats")
        # print(err)


print(divide(4, 2))  # 2
print(divide([],"1"))  # "Please provide two integers or floats"
print(divide(1, 0))  # "Please do not divide by zero"

# print(divide(1, 2))
# print(divide(1, "a"))


