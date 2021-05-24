print("1번문제")

def flatten(data):
    for i in data:
        if type([i]):
            for j in i:
                print(j)
        else:
            print(i)


example = [[1, 2, 3], [4,[5, 6]], 7, [8, 9]]
print("원본 : ", example)
print("변환 : ", flatten(example))



