tuple_test1 = (10, 20, 30)
tuple_test2 = 10, 20, 30
list_test1 = [1, 2, 3]

print("tuple_test1", tuple_test1, type(tuple_test1), end="\n\n")
print("tuple_test3", tuple_test2, type(tuple_test2), end="\n\n")
print("list_test1", list_test1, type(list_test1), end="\n\n")

list_test1[1] = 10
print("list_test1", list_test1, type(list_test1), end="\n\n")

tuple_test1[1] = 100
print("tuple_test1", tuple_test1, type(tuple_test1), end="\n\n")
