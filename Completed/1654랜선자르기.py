# 백준 1654 랜선 자르기 실버2
# 핵심 알고리즘 = 매개변수 탐색 (이진 탐색 응용 알고리즘)
'''
아잔 텀색을 통해 조건을 만족하는 최대값을 활용하는 알고리즘.

1. 정답을 매개 변수로 만들고, Yes/No 문제(결정 문제)로 바꿔 보기
2. 모든 값에 대해서 Yes/No를 채웠다고 생각했을 때, 정렬된 상태인가?
3. Yes/No를 결정하는 문제로 풀기

· 문제를 거꾸로 푸는 것이기 때문에 통찰력이 요구된다.
· 최근 코딩테스트 빈도로 굉장히 높게 나온다.
· 키워드에 "~~의 최댓값/최솟값 을 구하시오"가 포함되면 매개 변수 탐색을 접근해볼 가치가 있다. 
'''

# 파이썬에서 정렬 알고리즘으로 사용하는 Timsort = 평균 nlogn
# 파이썬 최대값 알고리즘 n
# https://wiki.python.org/moin/TimeComplexity
# 평균적으론 정렬하고 최댓값을 찾는게 더 효율적

from sys import stdin
inputF = stdin.readline

def Parametric_Search(Lis: list, N: int):
    Lis.sort()
    start = 0      # 무조건 가능한 값
    end = Lis[-1]  # 리스트 내의 최댓값으로 시작
    mid = end
    
    while True:  # 이진 탐색 마지막까지 순회
        cnt = 0
    
        for value in Lis:
            cnt += (value//mid)
            #print(f"cnt = {cnt}")
        
        if N > cnt:
            end = mid
            #print(f"end change = {end}")
        elif N <= cnt:
            start = mid
            #print(f"start change = {start}")
        
        mid = (start+end)//2
        if mid == start:
            break

    return start


if __name__ == '__main__':
    K, N = map(int,inputF().split())
    LanList = []
    for _ in range(K):
        LanList.append(int(inputF())) 

    rtn = Parametric_Search(LanList, N)  
    print(rtn)


'''
import sys

K, N = map(int, sys.stdin.readline().split())

l = [int(sys.stdin.readline()) for _ in range(K)]

def func(x):
    return sum([i//x for i in l])

left, right = 0, 2**31
while left < right:
    mid = (left+right) // 2
    if func(mid) >= N:
        left = mid+1
    else:
        right = mid

print(left-1)
'''