donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0)

total_donations = 0
for donation in donations.values():
    total_donations += donation

print(f"total donations = {total_donations}")

total_donations = sum(donation for donation in donations.values())
print(f"total donations = {total_donations}")

total_donations = sum(donations.values())
print(f"total donations = {total_donations}")

print("sam" in donations)

if "sam" in donations:
    print(f"the value is {donations['sam']}")
else:
    print("it doesn't exist")


instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}

print(instructor)

# add a value
instructor["city"] = "boulder"
print(instructor)


# Dictionary Comprehension
numbers = dict(first=1, second=2, third=3)
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)   # {'first': 1, 'second': 4, 'third': 9}

str1 = "ABC"
str2 = "123"
combo = {str1[i]: str2[i] for i in range(0, len(str1))}
print(combo)  # {'A': '1', 'B': '2', 'C': '3'}

# Dictionary Comprehension Conditional Logic
num_list = [1, 2, 3, 4]
odd_even = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(odd_even)   # {1: 'odd', 2: 'even', 3: 'odd', 4: 'even'}

# combine two lists using Dictionary Comprehension
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

answer = {list1[i]: list2[i] for i in range(0, len(list1))}
print(answer)

# or using zip
answer2 = dict(zip(list1, list2))
print(answer2)

# create a dict object from a list of list
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer = {person[i][0]: person[i][1] for i in range(0, len(person))}
print(answer)

# better answer one
answer = {thing[0]: thing[1] for thing in person}
print(answer)

# better answer two
answer = {k: v for k, v in person}
print(answer)

# best answer using dict()
answer = dict(person)
print(answer)

# create dict object mapping ascii charsw
answer = {i: chr(i) for i in range(65, 91)}
print(answer)
