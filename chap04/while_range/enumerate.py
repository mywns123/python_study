example_list = ["요소A", "요소B", "요소C"]

print("# 반복문과 조합하기")
for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))

example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C",
}

# 딕셔너리의 items() 함수
print("# 딕셔너리의 items() 함수")
print("items() : ", example_dictionary.items())
print()

# 딕셔너리의 items() 함수와 반복문 조합하기
print("# 딕셔너리의 items() 함수와 반복문 조합하기")
for key, element in  example_dictionary.items():
    print("dictionary[{}] = {}".format(key, element))

# list 내포
array = []
for i in range(0, 20, 2):
    array.append(i*i)
print(array)

array = [i * i for i in range(0, 20, 2)]
print(array)

array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]

print(output)

# 10진수의 변환
print("# 10진수의 변환")
# 10진수를 2진수로 변환
print("10 >> 2진수로", "{:b}".format(10))
# 2진수를 10진수로 변환
print("1010 >> 10진수로", int("1010", 2))
# 10진수를 8진수로 변환
print("10 >> 8진수로", "{:o}".format(10))
# 8진수를 10진수로 변환
print("12 >> 10진수로", int("12", 8))
# 10진수를 16진수로 변환
print("10 >> 16진수로", "{:x}".format(10))
# 16진수를 10진수로 변환
print("10 >> 10진수로", int("10", 16))

print("안녕안녕하세요".count("안"))


#
# output =
#
# for i in :
#     print("{} : {}".format(i, "{:b}".format(i)))
# print("합계 : ", sum(output))
#
