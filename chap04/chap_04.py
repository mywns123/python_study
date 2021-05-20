array = [273, 32, 103, "문자열", True, False]
print(array)

list_a = [273, 32, 103, "문자열", True, False]
print(list_a[0])

list_a[0] = "변경"
print(list_a)

print(list_a[3][0])

list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list_a[1])
print(list_a[1][1])

list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# 리스트")
print("list_a = ", list_a)
print("list_b = ", list_b)
print()

# 기본연산자
print("# 리스트 기본 연산자")
print("list_a + list_b = ", list_a + list_b)
print("list_a * 3 = ", list_a * 3)
print()

# 함수
print("#길이 구하기")
print("len(list_a) = ", len(list_a))

list_a = [1, 2, 3]

# 리스트 뒤에 요소 추가하기
print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a)
print()

# 리스트 중간에 요소 추가하기
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)

list_a = [1, 2, 3]
list_b = [4, 5, 6]
list_c = list_a + list_b

print("list_a = ",list_a)
print("list_b = ",list_b)
print("list_c = ",list_c)

list_a.extend(list_b)
print("list_a = ",list_a)
print("list_b = ",list_b)

list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거방법[1] - del
del list_a[1]
print("del list_a[1] : ", list_a)

# 제거방법[2] - pop()
list_a.pop(2)
print("pop(2) : ", list_a)

list_b = [0, 1, 2, 3, 4, 5, 6]
print(list_b)
del list_b[3:6]
print(list_b)

list_c = [1, 2, 1, 2]
print(list_c)
list_c.remove(2)
print(list_c)
list_c.clear()
print(list_c)

array = [273, 32, 103, 57, 52]
for element in array:
    print(element)






