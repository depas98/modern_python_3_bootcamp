def append(list):
    list.append(1)


def reassign(list):
    list = [0, 1]


def change_it(int1=-99, string1=""):
    int1 = -1
    string1 = "changed"
    print(f"in changeit func int1: {int1} string1: {string1}")


list = [0]
print(f"initial: {list}")

reassign(list)
print(f"reassign: {list}")

append(list)
print(f"append: {list}")

int1 = 0
string1 = "initial"

print(f"before int1: {int1} string1: {string1}")

change_it(int1, string1)

print(f"after int1: {int1} string1: {string1}")



