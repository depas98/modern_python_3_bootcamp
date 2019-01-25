def sum_all_nums(*nums):
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
