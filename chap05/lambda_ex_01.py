def print_hello():
    print("안녕하세요.")


def call_10_time(func):
    for i in range(10):
        func()


call_10_time(print_hello)