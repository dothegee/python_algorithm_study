# 실습 1-1
# 세 정수를 입력받아 최댓값 구하기

print("세 정수의 최댓값을 구합니다.")
a=int(input("정수 a의 값을 입력하세요. : ")) # input으로 받은 변수의 type 은 string이므로 int를 씌여 정수로 변환 
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
#실습 1-2
#최댓값 구하기 함수 작성
def max3(a, b, c):
    #a, b, c의 최댓값을 구하여 반환
    maximum = a
    if b > maximum:
        maximum=b
    if c > maximum:
        maximum=c
    return maximum

#실습 1-3
# 입력받은 정수의 부호(양수,음수,0) 출력하기
#실습 1-4
# 3개로 분기하는 조건문
# 분기는 프로그램의 실행 흐름을 다른 곳으로 변경하는 명령을 뜻함.-->조건문을 이용

n = int(input('정수를 입력하세요.: '))

if n > 0:
    print('이 수는 양수입니다.')
elif n < 0:
    print("이 수는 음수입니다.")
else:
    print("이 수는 0입니다.")


