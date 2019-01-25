def return_day(day):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    try:
        int(day)
    except ValueError:
        print("Enter in number from 1 - 7")
        return None

    if 0 < day <= len(days):
        return days[day-1]
    return None


print(return_day('t'))


def last_element(list_in):
    # if len(list_in) == 0:
    #     return None
    # return list_in[len(list_in) -1]
    if list_in:
        return list_in[-1]
    return None


my_list = [1, 2, 4, 5]
print(last_element(my_list))
print(last_element("last item"))
print(last_element([]))


def single_letter_count(word, letter):
    return word.upper().count(letter.upper())


print(single_letter_count("test", "z"))
print(single_letter_count("test", "t"))


def multiple_letter_count(word):
    return {letter: word.count(letter) for letter in word}


print(multiple_letter_count("awesome"))  # {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}


def list_manipulation(list, command, location, value=0):
    if command == "remove":
        if location == "beginning":
            return list[0]
        elif location == "end":
            return list[-1]
    elif command == "add":
        if location == "beginning":
            list.insert(0, value)
        elif location == "end":
            list.append(value)

    return list


print(list_manipulation([1, 2, 3], "remove", "end"))  # 3
print(list_manipulation([1, 2, 3], "remove", "beginning"))  # 1
print(list_manipulation([1, 2, 3], "add", "beginning", 20))  # [20,1,2,3]
print(list_manipulation([1, 2, 3], "add", "end", 30))  # [1,2,3,30]


def is_palindrome(string=""):
    """
    A palindrom is a word or phrase which reads the same backward as forward

    :param string:
    :return:
    """

    if len(string) > 0:
        # remove all spaces, strip() just remove leading and trailing spaces
        stripped = string.replace(" ", "")
        return stripped == stripped[::-1]

    return False


print(is_palindrome('testing'))  # False
print(is_palindrome('tacocat'))  # True
print(is_palindrome('hannah'))  # True
print(is_palindrome('robert'))  # False
print(is_palindrome('amanaplanacanalpanama'))  # True


def frequency(search_list=[], search_item=None):
    return search_list.count(search_item)
    # if len(search_list) > 0 and type(search_list[0]) == type(search_item):
    #     return search_list.count(search_item)
    #
    # return 0


print(frequency([1, 2, 3, 4, 4, 4], 4))  # 3
print(frequency([True, False, True, True], False))  # 1
print(frequency([True, False, True, True], "what"))


def multiply_even_numbers(num_list):
    if len(num_list) == 0:
        return 0
    total = 1
    for number in num_list:
        if number % 2 == 0:
            total = number * total
    return total


print(multiply_even_numbers([2,3,4,5,6]))  # 48


def capitalize(string=""):
    return string[0].upper() + string[1::]


print(capitalize("tim"))  # "Tim"
print(capitalize("matt"))  # "Matt"


def compact(list=[]):
    return [value for value in list if value]


print(compact([0,1,2,"",[], False, {}, None, "All done"]))  # [1,2, "All done"]


def intersection(list1=[], list2=[]):
    return [value for value in list1 if value in list2]


print(intersection([1, 2, 3], [2, 3, 4]))  # [2, 3]
print(intersection(['a', 'b', 'z'], ['x', 'y', 'z']))  # ['z'


def partition(list1, bool_func):
    # two passes better to use a for loop
    # list_true = [value for value in list1 if bool_func(value)]
    # list_false = [value for value in list1 if not bool_func(value)]

    list_true = []
    list_false = []
    for value in list1:
        if bool_func(value):
            list_true.append(value)
        else:
            list_false.append(value)

    return [list_true, list_false]


def is_even(num):
    return num % 2 == 0


print(partition([1,2,3,4], is_even))  # [[2,4],[1,3]]
