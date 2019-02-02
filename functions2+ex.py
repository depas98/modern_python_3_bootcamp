def sum_all_nums(*nums):    # *num is a tuple
    print(nums)
    total = 0
    for val in nums:
        total += val
    return total


print(sum_all_nums(4, 6, 9, 4, 10))
print(sum_all_nums(4, 6, 9))


def contains_purple(*colors):
    if "purple" in colors:
        return True
    return False


print(contains_purple(25, "purple"))
print(contains_purple(1, 2, 3))


def favorite_colors(**kwargs):          # **kwargs is a dictionary
    for name, color in kwargs.items():
        print(f"{name}'s favorite color is {color}")


favorite_colors(Rusty='green', Colt='blue')


def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word


def combine_words2(word, kwargs):
    if "prefix" in kwargs:
        return kwargs["prefix"] + word
    elif "suffix" in kwargs:
        return word + kwargs["suffix"]
    return word


print(combine_words("child"))
print(combine_words("child", prefix="man"))
print(combine_words("child", suffix="ish"))
print(combine_words("child", suffix="er"))
print(combine_words("child", prefix="home"))

print(combine_words("child2", **{"prefix": "man"}))
print(combine_words2("child2", {"prefix": "man"}))


def count_sevens(*args):
    return args.count(7)


nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,
        34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,
        34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0]

result1 = count_sevens(1, 4, 7)
result2 = count_sevens(*nums)

print(result1)
print(result2)

def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # nope..

display_names(**names)  # "Colt says hello to Rusty"


def display_names(first, second):
    print(f"{first} says hello to {second}")


names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # nope..
display_names(**names)  # yup!


def add_and_multiply_numbers(a, b, c, **kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)


data = dict(a=1, b=2, c=3, d=55, name="Tony")

add_and_multiply_numbers(**data)  # 7
add_and_multiply_numbers(**data, cat="blue")  # 7


def display_info(a, b, *args, instructor="Colt", **kwargs):
    return [a, b, args, instructor, kwargs]


# [1, 2, (3,), 'Colt', {'job': 'Instructor', 'last_name': 'Steele'}]
print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))
print(display_info(1, 2, 3, instructor="Colt2", last_name="Steele", job="Instructor"))

# def calculate(make_float, operation, first, second, message="The result is"):
#     result = 0
#     if operation == "add":
#         if make_float:
#             result = float(first + second)
#         else:
#             result = first + second
#     elif operation == "subtract":
#         if make_float:
#             result = float(first - second)
#         else:
#             result = first - second
#     elif operation == "multiply":
#         if make_float:
#             result = float(first * second)
#         else:
#             result = first * second
#     elif operation == "divide":
#         if make_float:
#             result = float(first / second)
#         else:
#             result = first / second
#
#     return message + " " + str(result)

#  or using a dict lookup
def calculate(**kwargs):
    operation_lookup = {
        'add': kwargs.get('first', 0) + kwargs.get('second', 0),
        'subtract': kwargs.get('first', 0) - kwargs.get('second', 0),
        'divide': kwargs.get('first', 0) / kwargs.get('second', 1),
        'multiply': kwargs.get('first', 0) * kwargs.get('second', 0)
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    print(f"type: {type(operation_value)} value: {operation_value}")
    msg = kwargs.get('message', 'The result is')
    if is_float:
        final = f"{msg} {float(operation_value)}"
    else:
        final = f"{msg} {int(operation_value)}"
    return final


print(calculate(make_float=False, operation='add', message='You just added', first=2, second=4))  # "You just added 6"
print(calculate(make_float=True, operation='divide', first=3.5, second=5))  # "The result is 0.7"
