# 3번 문제
print("\n3번 문제")
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for number in numbers:
    print(number)

# 4번 문제
print("\n4번 문제")
charcter = {
    "name": "기사",
    "level": 12,
    "items": {"sword": "불꽃의 검", "armor": "풀플레이트"},
    "skill": ["베기", "세게 베기", " 아주 세게 베기"]
}

for key in charcter:
    if type(key) is list:
        print(key, ":",keyvalues())
    elif type(key) is dict:
        print(key, ":", charcter[key].values())
    else:
        print(key, ":", charcter[key])
