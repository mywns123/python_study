print("#하나만 출력1")
print()

print("#하나만 출력2", "abcd", sep="\n", end="\n\n")
print("결과", end="\n\n")

print(type('하나만'), type("하나만"), type(12), type(12.5), sep="\n", end="\n\n")

# print("안녕하세요" + 1)

print("안녕하세요"[0])
print("안녕하세요"[4])
print("안녕하세요"[-1])
print("안녕하세요"[-5])

print("안녕하세요"[1:4])
print("안녕하세요"[1:6])
print("안녕하세요"[:3])
print("안녕하세요"[3:])
print("안녕하세요"[1:-1])

hello = "안녕하세요"
print(type(hello), hello[:2], hello, sep='\n', end='\n\n')

print("안녕" + ("하세요"*3))

res = input("답정너~~")
print("입력한 답은", res)

a = "10 20 30 40 50".split(" ")
print(type(a), a, sep="\n")

x, y, z = 10, 20, 30
print(x, y, z, sep='\n')
x, y = y, x
print(x, y,  sep='\n')