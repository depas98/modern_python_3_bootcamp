from math import sqrt


def calculate_fibonacci(index):
    if index < 0:
        raise ValueError("Index values need to be positive")

    if index == 0:
        return 0

    if index < 3:
        return 1

    return calculate_fibonacci(index - 2) + calculate_fibonacci(index - 1)


def calculate_fibonacci2(index):
    return int(((1+sqrt(5))**index-(1-sqrt(5))**index)/(2**index*sqrt(5)))


def _fib():
    a, b = 0, 1
    while True:            # First iteration:
        yield a            # yield 0 to start with and then
        a, b = b, a + b    # a will now be 1, and b will also be 1, (0 + 1)


def calculate_fibonacci3(index):
    return list(zip(range(index+1), _fib()))[index][1]


def calculate_fibonacci4(index):
    list = [0, 1]

    for i in range(2, index + 1):
        list.append(list[i - 2] + list[i - 1])

    return list[index]


fib_values = [fib_value for fib_value in zip(range(36), _fib())]
print(f"fib values: {list(zip(range(36), _fib()))}")

# print('{i:3}: {f:3}'.format(i=index, f=fibonacci_number))


print("using recursion O(2^^n)")
print(f"0:  {calculate_fibonacci(0)}")
print(f"1:  {calculate_fibonacci(1)}")
print(f"2:  {calculate_fibonacci(2)}")
print(f"3:  {calculate_fibonacci(3)}")
print(f"4:  {calculate_fibonacci(4)}")
print(f"5:  {calculate_fibonacci(5)}")
print(f"6:  {calculate_fibonacci(6)}")
print(f"7:  {calculate_fibonacci(7)}")
print(f"8:  {calculate_fibonacci(8)}")
print(f"35: {calculate_fibonacci(35)}")

print("using floating point math calculation")
print(f"0:  {calculate_fibonacci2(0)}")
print(f"1:  {calculate_fibonacci2(1)}")
print(f"2:  {calculate_fibonacci2(2)}")
print(f"3:  {calculate_fibonacci2(3)}")
print(f"4:  {calculate_fibonacci2(4)}")
print(f"5:  {calculate_fibonacci2(5)}")
print(f"6:  {calculate_fibonacci2(6)}")
print(f"7:  {calculate_fibonacci2(7)}")
print(f"8:  {calculate_fibonacci2(8)}")
print(f"35: {calculate_fibonacci2(35)}")


print("using yield and zip")
print(f"0:  {calculate_fibonacci3(0)}")
print(f"1:  {calculate_fibonacci3(1)}")
print(f"2:  {calculate_fibonacci3(2)}")
print(f"3:  {calculate_fibonacci3(3)}")
print(f"4:  {calculate_fibonacci3(4)}")
print(f"5:  {calculate_fibonacci3(5)}")
print(f"6:  {calculate_fibonacci3(6)}")
print(f"7:  {calculate_fibonacci3(7)}")
print(f"8:  {calculate_fibonacci3(8)}")
print(f"35: {calculate_fibonacci3(35)}")

print("iterating over a loop O(n)")
print(f"0:  {calculate_fibonacci4(0)}")
print(f"1:  {calculate_fibonacci4(1)}")
print(f"2:  {calculate_fibonacci4(2)}")
print(f"3:  {calculate_fibonacci4(3)}")
print(f"4:  {calculate_fibonacci4(4)}")
print(f"5:  {calculate_fibonacci4(5)}")
print(f"6:  {calculate_fibonacci4(6)}")
print(f"7:  {calculate_fibonacci4(7)}")
print(f"8:  {calculate_fibonacci4(8)}")
print(f"35: {calculate_fibonacci4(35)}")