# 실습 1-1
# 세 정수를 입력받아 최댓값 구하기

print("세 정수의 최댓값을 구합니다.")
a=int(input("정수 a의 값을 입력하세요. : "))
b=int(input("정수 b의 값을 입력하세요. : "))
c=int(input("정수 c의 값을 입력하세요. : "))

maximum = a # 단순 대입문
if b>maximum: # 조건식
    maximum = b
if c>maximum:
    maximum = c
# 9~13행은 순차적으로 실행
# -->> 순차구조
# 10~13행은 조건식으로 평가한 결과에 따라 프로그램의 실행 흐름이 변경
# -->> 선택구조

print(f"최댓값은 {maximum}입니다.")

# 이름을 입력받아 인사하기
print("이름을 입력하세요. : ", end=" ") #if end=" "가 없으면 23행 실행시 다음줄에 출력이 됨.
name = input()
print(f"안녕하세요? {name} 님")

name = input("이름을 입력하세요. : ")
print(f"안녕하세요? {name} 님")

a=input()
print(type(a))