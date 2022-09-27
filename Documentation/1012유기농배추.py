# 백준 1012 유기농 배추   실버2
# 그래프이론, DFS, BFS

import sys
sys.setrecursionlimit(10**6)  # 재귀 제한에 의한 런타임 오류 방지
inputF = sys.stdin.readline   # 입출력 속도 개선

def DFS(field, x, y):
    # 인덱스가 벗어나는 경우에 즉시 return
    if x < 0 or y < 0 or x >= N or y >= M:
        return 0
    # 해당 위치가 1이라면 인접한 곳에 1이 있는지 재귀(DFS)
    elif field[x][y] == 1: 
        field[x][y] = 0
        DFS(field, x-1, y)
        DFS(field, x+1, y)
        DFS(field, x, y-1)
        DFS(field, x, y+1)
        return 1

T = int(inputF())
for _ in range(T):
    # M:가로(열), N:세로(행), K:배추개수
    M, N, K = map(int, inputF().split())

    # 배추밭
    field = [[0 for col in range(M)] for _ in range(N)]

    # 배추 위치
    for i in range(K):
        # x:열, y:행
        x, y = map(int, inputF().split())
        field[y][x] = 1

    total = 0
    for i in range(N): # 세로 반복
        for j in range(M): # 가로 반복
            if DFS(field, i, j):
                total += 1 

    print(total)