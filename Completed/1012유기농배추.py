# 백준 1012  유기농 배추  실버2
# 그래프이론 (너비 탐색, 깊이 탐색)
'''
최소 5마리의 배추흰지렁이가 필요하다. 
0은 배추가 심어져 있지 않은 땅이고, 
1은 배추가 심어져 있는 땅을 나타낸다.

1	1	0	0	0	0	0	0	0	0
0	1	0	0	0	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	0	0	1	0	0	0	0	0
0	0	1	1	0	0	0	1	1	1
0	0	0	0	1	0	0	1	1	1

'''
import sys
inputF = sys.stdin.readline
sys.setrecursionlimit(10**6)
T = int(inputF())  # 테스트 케이스 개수


def Searching(n, m):
    global M, N
    print(f"{M=}, {N=}... {n=} {m=}")
    if field[n][m] == 0:
        return
    else:
        field[n][m] = 0
        if  n == N-1 and m == M-1 :
            Searching(n-1, m)
            Searching(n, m-1)
        elif n == N-1 and m == 0:
            Searching(n-1, m)
            Searching(n, m+1)
        elif n == 0 and m == M-1:
            Searching(n+1, m)
            Searching(n, m-1) 
        elif n > 0 and m == 0:
            Searching(n-1, m)
            Searching(n+1, m)
            Searching(n, m+1)
        elif n == 0 and m == 0:
            Searching(n+1, m)
            Searching(n, m+1)
        elif n > 0 and m == M-1:
            Searching(n-1, m)
            Searching(n+1, m)
            Searching(n, m-1)
        elif n == 0 and m > 0:
            Searching(n+1, m)
            Searching(n, m+1)
            Searching(n, m-1)
        elif n == N-1 and m > 0:
            Searching(n-1, m)
            Searching(n, m+1)
            Searching(n, m-1)
        else:
            Searching(n-1, m)
            Searching(n, m-1)
            Searching(n+1, m)
            Searching(n, m+1) 

for _ in range(T):
    global M, N
    M, N, K = map(int, inputF().split())
    field = [[0]*M for _ in range(N)]   # 밭 구조
    # M = 가로, N = 세로, K = 배추 개수
    cnt = 0

    for _ in range(K):
        A, B = map(int, inputF().split())
        field[B][A] = 1


    for n in range(N):
        for m in range(M):
            print("%3d" % (field[n][m]), end=' ')
        print()


    for n in range(N):
        for m in range(M):
            if field[n][m] == 1:
                cnt += 1
                Searching(n,m)

    print(cnt)
    
'''
# 너비 우선 탐색 적용 코드

import sys
from collections import deque
def bfs(y,x): # 영역 확인
    q = deque()
    q.append((y,x))
    while q:
        now = q.popleft()
        for l in range(4): # 사방면 확인
            hh = now[0] + dh[l]
            ww = now[1] + dw[l]
            if 0 <= ww < w and 0 <= hh < h and graph[hh][ww] == 1:
                graph[hh][ww] = 0
                q.append((hh,ww))

if __name__ == "__main__":
    dw = [0,1,0,-1] # 북, 동, 남, 서
    dh = [-1,0,1,0]
    read = sys.stdin.readline
    T = int(read())
    for _ in range(T):
        w, h, k = map(int,read().split())
        graph = [[0]*w for _ in range(h)]
        result = 0
        for _ in range(k): # 배추 위치 입력
            x,y = map(int,read().split())
            graph[y][x] = 1
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    bfs(i,j)
                    result += 1 # 영역 수
        print(result)
'''