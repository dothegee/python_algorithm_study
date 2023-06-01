from typing import Any, Sequence

# 이진 검색
# 정렬된 배열에서 검색

def bin_search(a:Sequence,key:Any):
    # 시퀀스 a 에서 key와 일치하는 원소를 이진 검색
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2 # 중앙 원소의 인덱스
        if a[pc]==key:
            return pc
        elif a[pc]<key:
            pl = pc + 1
        else:
            pr = pc - 1
        
        if pl > pr :
            break

    return -1


# if __name__=="__main__":
#     num = int(input("원소 수 입력 : "))
#     x = [None]*num

#     print('배열 데이터를 오름차순으로 입력')

#     x[0]=int(input('x[0] : '))
#     for i in range(1,num):
#         while True:
#             x[i] = int(input(f"x[{i}] : "))
#             if x[i] >= x[i - 1]:
#                 break
    
#     ky = int(input('검색할 값을 입력 : '))

#     idx = bin_search(x,ky)

#     if idx == -1:
#         print("검색값을 갖는 원소가 존재하지 않습니다.")
#     else:
#         print(f"검색값은 x[{idx}]에 있습니다")

####################################
############## 복잡도 ##############
####################################
# 시간 복잡도 : 실행하는 데 필요한 시간을 평가
# 공간 복잡도 : 메모리(기억 공간)와 파일 공간이 얼마나 필요한지를 평가

# 실습 3C-3
# 이진 검색 알고리즘의 실행 과정을 출력

def bin_search_process(a:Sequence, key:Any)->int:
    # 시퀀스 a에서 key와 일치하는 원소를 이진 검색(실행과정 출력)

    pl = 0
    pr = len(a) - 1

    print('   |',end="")
    for i in range(len(a)):
        print(f"{i:4}", end="")
    print()
    print("---+"+(4*len(a)+2)*"-")

    while True:
        pc = (pl + pr) // 2

        print("   |", end="")
        if pl != pc :
            print((pl*4+1)*" "+"<-"+((pc-pl)*4)*" "+"+", end="")
        else:
            print((pc*4+1)*" "+"<+",end="")
        
        if pc != pr:
            print(((pr-pc)*4-2)*" "+"->") 
        else:
            print("->")
        
        print(f"{pc:3}|", end="")
        for i in range(len(a)):
            print(f"{a[i]:4}", end="")
        print("\n   |")
        if a[pc]==key:
            return pc
        elif a[pc]<key:
            pl = pc + 1
        else:
            pr = pc - 1
        
        if pl > pr :
            break

if __name__=="__main__":
    num = int(input("원소 수 입력 : "))
    x = [None]*num

    print('배열 데이터를 오름차순으로 입력')

    x[0]=int(input('x[0] : '))
    for i in range(1,num):
        while True:
            x[i] = int(input(f"x[{i}] : "))
            if x[i] >= x[i - 1]:
                break
    
    ky = int(input('검색할 값을 입력 : '))

    idx = bin_search_process(x,ky)

    if idx == -1:
        print("검색값을 갖는 원소가 존재하지 않습니다.")
    else:
        print(f"검색값은 x[{idx}]에 있습니다")