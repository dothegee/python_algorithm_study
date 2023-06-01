from typing import Any, Sequence
import copy
# 실습 3-1
# while 문으로 작성한 선형 검색 알고리즘
def seq_search(a:Sequence, key : Any)->int:
    # 시퀀스 a 에서 key 와 값이 같은 원소를 선형 검색(while)
    i = 0

    while True:
        if i == len(a):
            return -1 # 검색을 실패하면 -1을 리턴
        if a[i] == key:
            return i
        i += 1

if __name__ == "__main__":
    num = int(input("원소 수를 입력 : "))
    x = [None]*num
    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))

    ky = int(input('검색할 값을 입력 : '))

    idx = seq_search(x, ky)

    if idx == -1:
        print("검색값이 없음")

    else:
        print(f"검색값은 x[{idx}]")

# 실습 3-2
# for 문으로 작성한 선형 검색 알고리즘
def seq_search_for(a:Sequence, key:Any)->int:
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1

num = int(input("원소 수를 입력 : "))
x = [None]*num
for i in range(num):
    x[i] = int(input(f"x[{i}] : "))

ky = int(input('검색할 값을 입력 : '))

idx = seq_search_for(x, ky)

if idx == -1:
    print("검색값이 없음")

else:
    print(f"검색값은 x[{idx}]")

# 배열 맨 앞부터 순서대로 원소를 스캔하는 선형 검색은 
# 원소의 값이 정렬되지 않은 배열에서 검색할 때 사용하는 유일한 방법

###############################################
################## 보초법 #####################
###############################################
# 선형 검색은 반복할 때마다 2가지 종료조건ㅇ르 체크
# 단순한 판단이지만 이 과정을 계속 반복하면 종료 조건을 검사하는 비용을 무시할 수 없음
# 검색할 값을 배열의 맨 끝에 추가
# 검색할 값과 같은 원소를 발견해야 하므로 맨 끝에 도달했는지 판단은 할 필요 없음

# 실습 3-3

def seq_search_sentinel(seq:Sequence, key:Any)->int:
    # 시퀀스 seq에서 key와 일치하는 원소를 선형 검색(보초법)
    a = copy.deepcopy(seq) # seq를 복사
    a.append(key) # 보조 key를 추가

    i=0
    while True:
        if a[i]==key:
            break
        i+=1
    return -1 if i ==len(seq) else i

if __name__=="__main__":
    num = int(input('원소 수를 입력 : '))
    x = [None]*num

    for i in range(num):
        x[i] = int(input(f"x[{i}] : "))

    ky=int(input('검색할 값은 ? '))

    idx = seq_search_sentinel(x,ky)

    if idx == -1:
        print('검색값을 갖는 원소가 존재하지 않습니다.')
    else:
        print(f"검색값은 x[{idx}]")