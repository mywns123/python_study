import test_module as test

if __name__ == "__main__":
    radius = test.number_input()
    print(test.get_circumference(radius))
    print(test.get_circle_area(radius))
