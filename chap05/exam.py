# def dan(num):
#     for i in range(1, 10):
#         print("{} * {} = {:2}".format(num, i, num*i))
# if __name__=="__main__":
#     dan(3)
# def gugudan():
#     for i in range(2, 10):
#         dan(i)
# if __name__=="__main__":
#     gugudan()

print("#1번 문제")
def gugu():
	for j in range(1, 10):
		print()
		for i in range(2, 10):
			print("{} * {} = {:2}".format(i, j, i*j), end="	  ")


if __name__ == "__main__":
	gugu()


print("\n#2번 문제")
def solution(array, commands):
	answer = []
	for i in range(0, len(commands)):
		c = array[commands[i][0]-1:commands[i][1]]
		d = sorted(c)[commands[i][-1]-1]
		answer.append(d)
	return answer


def solution2(array, commands):
	answer = []
	for a, b, c in commands:
		answer += [sorted(array[a-1:b])[c-1]]
	return answer

def solution3(array, commands):
	return [sorted(array[a-1:b])[c-1] for a, b, c in commands]



if __name__ == "__main__":
	array = [1, 5, 2, 6, 3, 7, 4]
	commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
	result = solution(array, commands)
	print(type(result), result)


print("\n#3번 문제")
list_a = [[10, 20], [30, 40, 70, 110], [50, 60], [80, 90, 100]]
dict_a = {'k': {'a': 10, 'b': 20}, 'l': {'a': 10, 'b': 20, 'c': 40}, 'm': {'a': 10}}

for key, element in dict_a.items():
	print("\n{} == > ".format(key), end=' ')
	for e, k in element.items():
		print("{} : {}".format(e, k), end=', ')


for i in range(0, len(list_a)):
	print()
	for j in list_a[i]:
		print(j, end=' ')


