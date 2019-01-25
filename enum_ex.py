from enum import Enum     # for enum34, or the stdlib version
# from an num import Enum  # for the a enum version
Animal = Enum('Animal', 'ant bee cat dog')

print(Animal.ant)  # returns <Animal.ant: 1>
print(Animal['ant'])  # returns <Animal.ant: 1> (string lookup)
print(Animal.ant.name)  # returns 'ant' (inverse lookup)
print(Animal.dog.name)  # returns 'dog' (inverse lookup)


class Color(Enum):
    red = 1
    green = {"index": "2", "name": "green"}
    blue = [2, 4]


print(Color.red)
print(repr(Color.red))
print(Color.red.name)
print(Color.red.value)
print(Color.green.value)
print(Color.blue.value)