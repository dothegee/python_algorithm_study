#다른 파일에서 import 하는 연습하기 위한 파일

from typing import Any, Sequence
#건네받는 매개변수 a의 자료형은 Sequence
#반환하는 것은 임의의 자료형인 Any
def max_of(a : Sequence)->Any:
    # 시퀀스형 a 원소의 최댓값을 반환
    maximum = a[0]
    for i in range(1,len(a)):
        if a[i]>maximum:
            maximum = a[i]
    return maximum

if __name__=='__main__':
    print('배열의 최댓값을 구합니다.')
    num = int(input('원소 수를 입력하세요 : '))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))
    print(f"최댓값은 {max_of(x)}")
