# 백준 11650 좌표 정렬하기  실버5
# 정렬
'''
https://www.acmicpc.net/problem/11650

2차원 평면 위의 점 N개가 주어진다. 
좌표를 x좌표가 증가하는 순으로, 
x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
'''
from sys import stdin
inputF = stdin.readline
N = int(inputF())
Point_List = []

for _ in range(N):
    Point_List.append(list(map(int, inputF().split())))

Point_List.sort(key=lambda x: (x[0], x[1]))

for i in Point_List:
    print(i[0], i[1])


'''
import sys
input = sys.stdin.readline

n = int(input().rstrip())

res = []

for _ in range(n):
    x, y = map(int, input().rstrip().split())
    res.append((x, y))

res.sort()

for tup in res:
    print(' '.join(map(str, tup)))

'''