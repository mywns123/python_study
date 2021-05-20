dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print("name: ", dictionary["name"])
print("type: ", dictionary["type"])
for ingredient in dictionary["ingredient"]:
    print("ingredient: ", ingredient)
print("origin: ", dictionary["origin"])
print()

dictionary["name"] = "8D 건조 망고"
print("name:", dictionary["name"])

# 값 추가하기
dictionary["price"] = 5000
print(dictionary)

# 값 변경하기
dictionary["name"] = "8D 건조 파인애플"
print(dictionary)

# 값 제거하기
del dictionary["ingredient"]
print(dictionary)

# 접근하고자하는 키가 존재하는 경우에만 값을 출력
key = input(">접근 하고자 하는 키:")
if key in  dictionary:
    print(dictionary[key])
else:
    print("존재하지 않는 키에 접근하고 있습니다.")

# 접근하고자하는 키가 존재하지않는 경우 None출력
key = input(">접근 하고자 하는 키:")
value = dictionary.get(key)
print("값 : ", value)

if value == None:
    print("존재하지 않는 키에 접근하고 있습니다.")

# for 반복문을 사용합니다.
for key in dictionary:
    print(key, ":", dictionary[key])