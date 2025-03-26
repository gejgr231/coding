from sys import getsizeof
"""
print("hello", "word") #hello word
print()
print("hello", "word", sep="")#helloword
print("hello", end="")#helloword
print("word")

singer = input("좋아하는 가수는?")
print("좋아하는 가수는?", singer, "입니다")
#좋아하는 가수는? 뉴진스 입니다


a,b,c =1,1.31,"hello"
print(a, b, c)

python_world = 10 #smake_case
print((100-2)/7+9*3)

num =10
num += 20 # num = num + 20 -> num = 10 + 20
print(num)

print(2 > 1) #-> ture


num =3
num %= 2
print("true면 짝수, False면 홀수:", num == 0)


#3/25
name = "jin"
print(type(name))

#자료형
#딕셔너리형 -> 사전과 비슷
print(getsizeof(1)) #28 단위: 바이트

형변환이란 데이터 타입을 다른 타입으로 변환하는 과정
• 자동 형변환 : 암묵적으로 데이터 타입 변환
• 정수와 실수 연산 : 정수와 실수가 함께 연산되면 정수가 실수로 자동 변환
• 명시적 형변환 : 개발자가 명시적으로 형변환
• int() : 실수나 문자열의 숫자를 정수로 변환
• float() : 정수나 문자열을 숫자를 실수로 변환
• str() : 문자열로 변환
• 단, 형변환시 데이터 손실이 될 수 있음.
• 예) 실수를 정수로 형변환시 소수점 이하는 잘려 나감


num = input("숫자입력 하세요")
print(num) #num은 input으로 인해 str 타입임! -> not 정수형
a= int(num)%2 #num을 정수형으로 형변환
print(a)


a, b = map(int, input().strip().split(' ')) # strip -> 양 사이드의 공백만 없애줌


number = "저는 올해 %d살입니다." % 20
print(number)

• 사용법
• %d 는 정수
• %f 는 실수
• %s 는 문자열
• %c 는 문자
• %뒤 숫자는 문자열 길이
• %.숫자는 소수점 자리수

text = "{}점수: {}점, {}점수:{}점".format("영어", 100, "수학", 90)
print(text)
#f문자열 포매팅
name = '홍길동'
age = 20
text =f'내 이름은 {name}입니다. 나이는 {age +1}살 입니다.'

"""
a = """
ㅣ\\_/ㅣ
ㅣq pㅣ   /}
(  0  )\"\"\"\\
ㅣ\"^\"\'     ㅣ
ㅣㅣ_/=\\\\__ㅣ"""

"""
print(a)
my_name = '김진수'
print(f'{my_name:=^20}')
name = '중괄호'
b = f'문자열 실습입니다. "{{{name}}}"를 출력해보세요'
print(b)

#• 모든 인덱스는 앞에서는 항상 0부터 시작. 뒤에서는 -1부터 시작
a = "Hello, Python"
print(a[7])

print(a.index('o'))

print(a.replace("Hello","안녕"))

#문자열 판별하기(숫자판펼)
#• isdigit() : 10진수 및 일부 유니코드 숫자 포함. isdecimal()보다 넓은 범위

#1번
name = "홍길동"
print(f'이름을 입력하세요.{name}')

age = 100
print(f'나이를 입력하세요.{age}')
print(f'안녕하세요! {name}님 ({age}세)')

#2번
year = 2010
print(f'태어난 년도를 입력하세요.{year}')
now_year = 2023
print(f'올해 년도를 입력하세요.{now_year}')
print(f'올해는{now_year}년,{name}님의 나이는 {now_year-year+1}세 입니다')


# 실습
# 입출력 실습 - 다음과 같이 실행되도록 코드를 작성하세요.

name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: "))

print(f"안녕하세요. {name}님! 당신의 나이는 {age}살입니다.")


# 실습2
# 입출력 실습 - 다음과 같이 실행되도록 코드를 작성하세요.

name = input("이름을 입력하세요: ")
year = int(input("태어난 년도를 입력하세요: "))
now = int(input("현재 년도를 입력하세요: "))

print(f"안녕하세요. {name}님! 당신은 {now - year + 1}살입니다.")

"""

