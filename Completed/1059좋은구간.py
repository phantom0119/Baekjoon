# 백준 1059 좋은 구간  실버5

# 수학, 브루트포스, 정렬

'''
정수 집합 S가 주어졌을때, 다음 조건을 만족하는 구간 [A, B]를 좋은 구간이라고 한다.

A와 B는 양의 정수이고, A < B를 만족한다.
A ≤ x ≤ B를 만족하는 모든 정수 x가 집합 S에 속하지 않는다.
집합 S와 n이 주어졌을 때, n을 포함하는 좋은 구간의 개수를 구해보자.


4
1 7 14 10
2                   --> [2,3], [2,4], [2,5], [2, 6]   4

5
4 8 13 24 30
10                  --> [9, 10], [9, 11], [9, 12], [10, 11], [10, 12]  5

'''
import sys

cnt = int(input()) # 원소 개수
nList = list(map(int, sys.stdin.readline().split()))  # 원소 리스트
n = int(input())   # 구간 포함 
MinNumber = 1 # 가능한 최소
MaxNumber = 1000 # 가능한 최대

for num in nList:
    if num == n:  # 비교 수가 구간에 포함되면 종결
        print(0)
        sys.exit(0)

    # 최대 구간을 만들 수 있는 범위 찾기
    if num > MinNumber and num < n:  
        MinNumber = num
    elif num <= MaxNumber and num > n:
        MaxNumber = num-1

for i in range(MinNumber, n+1):  # 2-1
    if i in nList: pass
    else: MinNumber = i; break


Section = 0    
while MinNumber <= n:
    diff = (n-1) - MinNumber
    
    if diff < 0:
        Section += MaxNumber-MinNumber 
    else: 
        Section += MaxNumber-MinNumber-diff
    
    MinNumber += 1

#print(f"{MinNumber=}, {MaxNumber=}, {Section=}")
print(Section)

'''
from sys import stdin
input = stdin.readline

s = int(input())
l = list(map(int, input().split()))
l.append(0)
l.sort()
n = int(input())
tmp = 0
for i in range(s):
    if l[i] == n or l[i+1] == n:
        tmp = 0
        break
    elif l[i] < n < l[i+1]:
        tmp = (n - l[i]) * (l[i+1] - n) - 1
        break

print(tmp)
'''

