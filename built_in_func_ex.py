import sys

# all
print("*** all")
print(all([]))  # True
print(all([0, 1, 2, 3]))  # False
print(all([char for char in 'eio' if char in 'aeiou']))  # True
print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))  # True

people = ["Charlie", "Casey", "Cody"]
print([peeps[0] == 'C' for peeps in people])
print(all([peeps[0] == 'C' for peeps in people]))
people.append("Kacey")
print([peeps[0] == 'C' for peeps in people])
print(all([peeps[0] == 'C' for peeps in people]))

# can get rid of [], because w/o brackets it's a generator object so if you don't need a list back use it more efficient
print("*** all generator")
print(peeps[0] == 'C' for peeps in people)  # <generator object <genexpr> at 0x00B99FB0>
print(all(peeps[0] == 'C' for peeps in people))  #


def is_all_strings(l):
    return all(type(s) is str for s in l)


print(is_all_strings(['a', 'b', 'c']))
print(is_all_strings([2, 'a', 'b', 'c']))
print(is_all_strings(('hello', 'goodby')))

# any
print("\n*** any")
print(any([]))  # False
print(any([0, 1, 2, 3]))  # True
print(any([val for val in [1, 2, 3] if val > 2]))  # True
print(any([val for val in [1, 2, 3] if val > 5]))  # False

# A simple comparison of size (in Bytes)
list_comp = sys.getsizeof([x * 10 for x in range(1000)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000))

print("To do the same thing, it takes...")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")

# sorted
users = [
    {"username": "samuel", "tweets": ["I love cake", "I love pie", "hello world!"]},
    {"username": "katie", "tweets": ["I love my cat"]},
    {"username": "jeff", "tweets": [], "color": "purple"},
    {"username": "bob123", "tweets": [], "num": 10, "color": "teal"},
    {"username": "doggo_luvr", "tweets": ["dogs are the best", "I'm hungry"]},
    {"username": "guitar_gal", "tweets": []}
]

# To sort users by their username
sorted(users, key=lambda user: user['username'])

# Finding our most active users...
# Sort users by number of tweets, descending
print(sorted(users, key=lambda user: len(user["tweets"]), reverse=True))

# ANOTHER EXAMPLE DATA SET==================================
songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# To sort songs by playcount
print(sorted(songs, key=lambda s: s['playcount']))

names = ['Arya', "Samson", "Dora", "Tim", "Ollivander"]

# MIN MAX

# finds the minimum length of a name in names
min(len(name) for name in names)  # 3

# find the longest name itself
max(names, key=lambda n: len(n))  # Ollivander

songs = [
    {"title": "happy birthday", "playcount": 1},
    {"title": "Survive", "playcount": 6},
    {"title": "YMCA", "playcount": 99},
    {"title": "Toxic", "playcount": 31}
]

# Finds the song with the lowerest playcount
print(min(songs, key=lambda s: s['playcount']))  # {"title": "happy birthday", "playcount": 1})

# Finds the title of the most played song
print(max(songs, key=lambda s: s['playcount'])['title'])  # YMCA


def extremes(it):
    return min(it), max(it)


print(extremes([1, 2, 3, 4, 5]))
print(extremes((99, 25, 30, -7)))
print(extremes("alcatraz"))


# Return the highest magnitude in a list use abs and max
def max_magnitude(num_list):
    return max(abs(num) for num in num_list)


print(max_magnitude([300, 20, -900]))
print(max_magnitude([10, 11, 12]))
print(max_magnitude([-5, -1, -89]))


def sum_even_values(*args):
    return sum(num for num in args if num % 2 == 0)


print(sum_even_values(1, 2, 3, 4, 5, 6))
print(sum_even_values(4, 2, 1, 10))
print(sum_even_values(1))


def sum_floats(*args):
    return sum(arg for arg in args if type(arg) is float)


print(sum_floats(1.5, 2.4, 'awesome', [], 1))  # 3.9
print(sum_floats(1, 2, 3, 4, 5))  # 0


# zip examples

# unpacking (using *) with zip is very common when working with more complex data structures!
five_by_two = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*five_by_two)))  # [(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)]

midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ['dan', 'ang', 'kate']

# returns dict with {student:highest score} USING LIST COMP
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = {t[0]: max(t[1], t[2]) for t in zip(students, midterms, finals)}
print(final_grades)

# returns dict with {student:highest score} USING MAP+LAMBDA
# {'dan': 98, 'ang': 91, 'kate': 78}
final_grades = dict(
    zip(
        students,
        map(
            lambda pair: max(pair),
            zip(midterms, finals)
        )
    )
)

map_iterator = map(
    lambda pair: max(pair),
    zip(midterms, finals)
)
print(f"map iterator: {list(map_iterator)}")
print(final_grades)

# returns dict with student:average score
# {'dan': 89.0, 'ang': 90.0, 'kate': 65.5}
avg_grades = dict(
    zip(
        students,
        map(
            lambda pair: (pair[0] + pair[1]) / 2,
            zip(midterms, finals)
        )
    )
)
print(avg_grades)


def interleave(str1, str2):
    return "".join("".join(l) for l in zip(str1, str2))


print(interleave("hi", "ha"))
print(interleave("aaa", "zzz"))
print(interleave("lzr", "iad"))


# lambdas vs list comprehension
def triple_and_filter(l):
    # using list comprehension
    return [x * 3 for x in l if x % 4 == 0]


def triple_and_filter2(l):
    # using lambdas, with filter and map
    return list(map(
        lambda num: num * 3,
        filter(lambda num: num % 4 == 0, l)
    ))


print(triple_and_filter([1, 2, 3, 4]))  # [12]
print(triple_and_filter([6, 8, 10, 12]))  # [24,36]

print(triple_and_filter2([1, 2, 3, 4]))  # [12]
print(triple_and_filter2([6, 8, 10, 12]))  # [24,36]


def extract_full_name(l):
    return [f"{name['first']} {name['last']}" for name in l]


def extract_full_name2(l):
    return list(map(
        lambda name: f"{name['first']} {name['last']}",
        l
    ))


names = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name(names))  # ['Elie Schoppik', 'Colt Steele']
print(extract_full_name2(names))  # ['Elie Schoppik', 'Colt Steele']