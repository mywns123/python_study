import datetime

if True:
    print("True 입니다.")
    print("정말 true")

if False:
    print("FALSE")

print("aaa")

# 현재 날짜
now = datetime.datetime.now()

# 출력
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")

print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year, now.month,now.day, now.hour, now.minute, now.second))

# 오전 구분
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))
# 오후 구분
if now.hour >= 12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))

# 봄 구분
if 3 <= now.month <= 5:
    print("이번 달은 {}월로 봄입니다!".format(now.month))

# 여름 구분
if 6 <= now.month <= 8:
    print("이번 달은 {}월로 여름입니다!".format(now.month))

# 가을 구분
if 9 <= now.month <= 11:
    print("이번 달은 {}월로 가을입니다!".format(now.month))

# 겨울 구분
if now.month == 12 or 1 <= now.month <= 2:
    print("이번 달은 {}월로 겨울입니다!".format(now.month))
    
# 입력을 받습니다.
number = input("정수 입력 > ")
# 마지막 자리 숫자를 추출
last_character = number[-1]
# 숫자로 변환하기
last_numer = int(last_character)

# 짝수확인
if last_numer == 0 \
    or last_numer == 2 \
    or last_numer == 4 \
    or last_numer == 6 \
    or last_numer == 8:
    print("짝수입니다.")


# 홀수확인
if last_numer == 1 \
    or last_numer == 3 \
    or last_numer == 5 \
    or last_numer == 7 \
    or last_numer == 9:
    print("홀수입니다.")

# 입력을 받습니다.
number = input("정수 입력 > ")
last_character = number[-1]

# 짝수 조건
if last_character in "02468":
    print("짝수입니다.")

# 홀수 조건
if last_character in "13579":
    print("홀수입니다.")

# 입력을 받습니다.
number = input("정수 입력 >")
number = int(number)

# 짝수 조건
if number % 2 == 0:
    print("짝수 입니다.")
# 홀수 조건
if number % 2 == 1:
    print("홀수입니다.")

# 입력을 받습니다.
number = input("정수 입력 >")
number = int(number)

# 조건문을 사용합니다.
if number % 2 == 0:
    print("짝수 입니다.")
else:
    print("홀수입니다.")

month = now.month

# 조건문으로 계절을 확인합니다.
if 3 <= month <= 5:
    print("현재는 봄입니다.")
elif 6 <= month <= 8:
    print("현재는 여름입니다.")
elif 9 <= month <= 11:
    print("현재는 가을입니다.")
else:
    print("현재는 겨울입니다.")

# 변수를 선언합니다.
score = float(input("학점 입력 > "))

# 조건문을 적용합니다.
if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.2:
    print("현 체제의 수호자")
elif 2.8 <= score < 3.5:
    print("일반인")
elif 2.3 <= score < 2.8:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 2.3:
    print("오락문화의 선구자")
elif 1.0 <= score < 1.75:
    print("불가촉천민")
elif 0.5 <= score < 1.0:
    print("자벌레")
elif 0 <= score < 0.5:
    print("플랑크톤")
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗")

# 변수를 선언합니다.
score = float(input("학점 입력 > "))

# 조건문을 적용합니다.
if score == 4.5:
    print("신")
elif 4.2 <= score:
    print("교수님의 사랑")
elif 3.5 <= score:
    print("현 체제의 수호자")
elif 2.8 <= score:
    print("일반인")
elif 2.3 <= score:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score:
    print("오락문화의 선구자")
elif 1.0 <= score:
    print("불가촉천민")
elif 0.5 <= score:
    print("자벌레")
elif 0 <= score:
    print("플랑크톤")
else:
    print("시대를 앞서가는 혁명의 씨앗")


print("# if 조건문에 0넣기")
if 0:
    print("0은 True로 변환됩니다.")
else:
    print("0은 False로 변환됩니다.")
print()

print("# if 조건문에 빈 문자열 넣기")
if "":
    print("빈 문자열은 True로 변환됩니다.")
else:
    print("빈 문자열은 False로 변환됩니다.")

# 입력을 받습니다.
number = input("정수 입력 > ")
number = int(number)

# 조건문 사용
if number > 0:
    # 양수일때 : 아직 미구현 상태입니다.
    pass
else:
    # 음수일때 : 아직 미구현 상태입니다.
    pass

