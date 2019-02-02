
def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner


counter_inner = counter()
print([counter_inner() for i in range(1, 20)])


def counter2():
    counter.count = 0

    def inner():
        counter.count += 1
        return counter.count
    return inner


counter_inner = counter2()
print([counter_inner() for i in range(1, 20)])


def outer(a):
    def inner(b):
        return a+b
    return inner


result = outer(10)
print(result(20))  # 30
