from functools import reduce


def square(num): return num * num


print(square(9))

square2 = lambda num: num * num  # don't store in variable use def

print(square2(9))

add = lambda a, b: a + b
print(add(3, 10))

print(f"square func name: {square.__name__}")  # square
print(f"square2 func name: {square2.__name__}")  # lambda

cube = lambda x: x ** 3
print(cube(2))
print(cube(3))
print(cube(8))

# lambda map
nums = [2, 4, 6, 8, 10]
doubles = list(map(lambda x: x*2, nums))
print(doubles)

names = [
    {'first': 'Rusty', 'last': 'Steele'},
    {'first': 'Colt', 'last': 'Steele', },
    {'first': 'Blue', 'last': 'Steele', }
]

first_names = list(map(lambda x: x['first'], names))
print(first_names)  # ['Rusty', 'Colt', 'Blue']


def double(x): return x*2


doubles2 = list(map(double, nums))  # this looks a little cleaner
print(doubles2)


def decrement_list(nums):
    return list(map(lambda x: x - 1, nums))


print(decrement_list([1, 2, 3]))
print(decrement_list([19, 13, 10]))

# Return a new list with the string
# "Your instructor is " + each value in the array,
# but only if the value is less than 5 characters

names = ['Lassie', 'Colt', 'Rusty', "Bob"]
instructors = list(map(lambda name: f"Your instructor is {name}",
                       filter(lambda value: len(value) < 5, names)))

print(instructors)  # ['Your instructor is Colt', 'Your instructor is Bob']

# using list comprehension
instructors = [f"Your instructor is {name}" for name in names if len(name) < 5]
print(instructors)

l = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, l)
print(product)
l = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, l, 10)
print(total)


def remove_negatives(nums):
    return list(filter(lambda n: n >= 0, nums))


print(remove_negatives([-1, 3, 4, -99]))
