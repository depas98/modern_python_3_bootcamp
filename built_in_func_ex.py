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
min(songs, key=lambda s: s['playcount'])  # {"title": "happy birthday", "playcount": 1}

# Finds the title of the most played song
max(songs, key=lambda s: s['playcount'])['title']  # YMCA


def extremes(it):
    return min(it), max(it)


print(extremes([1, 2, 3, 4, 5]))
print(extremes((99, 25, 30, -7)))
print(extremes("alcatraz"))
