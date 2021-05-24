def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")


print_3_times()


def print_n_times(value, n):
    for i in range(n):
        print(value)


print_n_times("안녕하세요", 5)


def print_n_times(n, *values):
    for i  in range(n):
        for value in values:
            print(value)

        print()


print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그램")


def print_n_times(value, n=2):
    for i in range(n):
        print(value)


print_n_times("안녕하세요")


def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)

        print()


print_n_times("안녕하세요", "즐거운", "파이썬 프로그램", n=3)


def test(a, b=10, c=100):
    print(a+b+c)


test(10, 20, 30)
test(a=10, b=100, c=200)
test(c=10, a=100, b=200)
test(10, c=200)


def return_test():
    print("A 위치입니다.")
    return
    print("B 위치입니다.")


return_test()


def return_test():
    return 100


value = return_test()
print(value)


def return_test():
    return


value = return_test()
print(value)


def sum_all(start, end):
    output = 0
    for i in range(start, end+1):
        output += i

    return  output


print("0 to 100", sum_all(0, 100))
print("0 to 1000", sum_all(0, 1000))
print("50 to 100", sum_all(50, 100))
print("500 to 1000", sum_all(500, 1000))


def sum_all(start=0, end=100, step=1):
    output = 0
    for i in range(start, end +1, step):
        output += i

    return output


print("A", sum_all(0, 100, 10))
print("B", sum_all(end=100))
print("C", sum_all(end=100, step=2))
