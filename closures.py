# this is an example of a closure, n is included within the function increment
def increment():
    # Outside the scope of the returned function:
    n = 0

    def incrementor():
        nonlocal n
        # Without 'nonlocal' n += arg produces:
        # local variable 'n' referenced before assignment
        n += 1
        return n

    return incrementor


x = increment()
y = increment()

for i in range(5):
    print(x())

print("=" * 10)

for i in range(5):
    print(y())
