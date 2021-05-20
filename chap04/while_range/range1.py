a = range(5)
print(a)
a = list(range(10))
print(a)
a = list(range(0, 5))
print(a)
a = list(range(0, 10+1))
print(a)

n = 10
a = list(range(0, int(n/2)))
print(a)

a = list(range(0, int(n//2)))
print(a)

array = [273, 32, 103, 57, 52]
for i in range(len(array)):
    print("{}번째 반복 : {}".format(i, array[i]))

for i in  range(4, 0 - 1, -1):
    print("현재 반복 변수 : {}".format(i))

for i in reversed(range(5)):
    print("현재 반복 변수 : {}".format(i))
