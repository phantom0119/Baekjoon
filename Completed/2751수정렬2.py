# 백준 2751 수 정렬하기 2   실버5
# 병합정렬 (Merge Sort)
'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
'''
import sys
cnt = int(sys.stdin.readline())
arr = []
for _ in range(cnt):
    arr.append(int(sys.stdin.readline()))

def Merge_Sort(Lis : list):
    mid_idx = len(Lis)//2
    if mid_idx == 0:  # 값이 1개밖에 없으면 정렬 X
        return Lis
    # 정렬을 위해 2개 리스트로 분리
    Left = Lis[:mid_idx]
    Right = Lis[mid_idx:]
    #print(f"{Left=} {Right=}")

    Merge_Sort(Left)  # 2개의 값만 비교해서 붙는 과정이 필요함 (재귀)
    Merge_Sort(Right)

    left_idx = 0  # 왼쪽 정렬 시작 idx
    right_idx = 0 # 오른쪽 정렬 시작 idx
    complete_idx = 0  # 정렬 완료된 idx

    while left_idx < len(Left) and right_idx < len(Right):
        if Left[left_idx] < Right[right_idx]:
            #print("In First-1 While")
            Lis[complete_idx] = Left[left_idx]
            complete_idx += 1
            left_idx += 1
            #print(f"First-1 {Left=} {Right=} {arr=}")
        else:
            #print("In First-2 While")
            Lis[complete_idx] = Right[right_idx]
            complete_idx += 1
            right_idx += 1
           #print(f"First-2 {Left=} {Right=} {arr=}")           

    while left_idx < len(Left):  # 좌우 정렬 후 남은 인덱스 처리
        #print("In Second While")
        Lis[complete_idx] = Left[left_idx]
        complete_idx += 1
        left_idx += 1   
        #print(f"Second {Left=} {Right=} {arr=}")     
    
    while right_idx < len(Right):  # 왼족 남은 것 처리 후 마무리 오른쪽 처리
        #print("In Third While")
        Lis[complete_idx] = Right[right_idx]
        complete_idx += 1
        right_idx += 1    
        #print(f"Third {Left=} {Right=} {arr=}")    


Merge_Sort(arr)
for i in arr:
    print(i)


'''
# 엥? 그냥 sys 차이라고ㅡ,,??

import sys

n = int(input())
lst = []

for i in range(n):
    lst.append(int(sys.stdin.readline()))

lst.sort()
for i in lst:
    print(i)
'''