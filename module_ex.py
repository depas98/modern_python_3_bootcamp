from keyword import iskeyword


def contains_keyword(*args):
    for val in args:
        if iskeyword(val): return True
    return False


print(contains_keyword("hello", "goodbye"))
print(contains_keyword("def", "haha", "lol"))
