# 2
print("2번 문제")
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number >= 100:
        print("- 100 이상의 수 : ", number)

# 3
print("\n3번 문제")
numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

for number in numbers:
    if number % 2 == 0:
        print(number, "는 짝수입니다.")
    else:
        print(number, "는 홀수입니다.")

print()

for number in numbers:
    if number / 100 >= 1:
        print(number, "는 3 자릿수입니다.")
    elif number / 10 >= 1:
        print(number, "는 2 자릿수입니다.")
    else:
        print(number, "는 1 자릿수입니다.")

# 4
print("\n4번 문제")
list_of_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
for number in list_of_list:
    for num in number:
        print(num)

list_seq = [i for sub_list in list_of_list for i in sub_list]
print("list_seq : ", list_seq)

# 5
print("\n5번 문제")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
output = [[], [], []]

for number in  numbers:
    output[number % 3 - 1].append(number)

print(output)

# 6
print("\n추가 문제")
# 1 ~ 100까지 짝수만 list(even_list)에 저장하고 출력하시오
even_list = [i for i in range(1, 101) if i % 2 == 0]
print(even_list)

# 1 ~ 100까지 홀수만 list(odd_list)에 저장하고 출력하시오
odd_list = [i for i in range(1, 101) if i % 2 == 1]
print(odd_list)
