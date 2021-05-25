"""
def power(item):
    return item * item
"""
"""
power = lambda x: x * x
"""
"""
def under_3(item):
    return item < 3
"""
"""
under_3 = lambda x: x < 3
"""
list_input_a = [1, 2, 3, 4, 5]


# map()함수 사용
output_a = map(lambda x: x * x, list_input_a)
print(list(output_a))

# filter
output_b = filter(lambda x: x < 3, list_input_a)
print(list(output_b))


output_c = lambda x, y: x * y
res = output_c(5, 3)
print(res)
