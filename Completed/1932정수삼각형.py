# 백준 1932 정수삼각형

'''
        7
      3   8
    8   1   0
  2   7   4   4
4   5   2   6   5

--> 30

아래에 있는 수 중 하나를 선택하여 아래층으로 내려올 때, 
이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램을 작성하라. 

아래층에 있는 수는 

현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택할 수 있다.
'''

import sys
cnt = int(input())
TreeList = []  # 2차원 배열로 트리구조 저장

for i in range(cnt): # 값 층으로 받아오기  * 역순
    TreeList.insert(0, list(map(int, sys.stdin.readline().split()))) 
#print(f"{TreeList=}")

# bottom-up 방식? 같은 느낌으로 맨 아래부터 해서 큰수를 올림
for i in range(cnt):
    for j in range(cnt-1-i):
        TreeList[i+1][j] = max(TreeList[i+1][j] + TreeList[i][j] \
                                ,TreeList[i+1][j] + TreeList[i][j+1])

print(TreeList[-1][0])


