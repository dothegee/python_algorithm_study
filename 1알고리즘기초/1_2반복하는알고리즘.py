#실습1-7
#1부터 n까지 정수의 합 구하기1(while 문)
print("1부터 n까지 정수의 합")
n = int(input("n의 값을 입력 : "))

sum = 0
i = 1

while i <= n: #i가 n 보다 작거나 같을 동안 반복
    sum += i
    i += 1

print(f"{n}까지 정수 합은 {sum}")

#실습 1-8
# for문

sum = 0

for i in range(1,n+1):
    sum += i

print(f"{n}까지 정수 합은 {sum}")
