# 1번문제
print("1번문제")


def f(x):
    return (2 * x) + 1


print(f(10))


def f(x):
    return (x * x) + (2 * x) + 1


print(f(10))

# 2번문제
print("2번문제")


def mul(*values):
    i = 1
    for value in values:
        i *= value

    return i


print(mul(5, 7, 9, 10))
