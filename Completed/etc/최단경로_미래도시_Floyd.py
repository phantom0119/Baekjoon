# 코딩 테스트(파이썬) 최단경로 문제 연습
# 미래도시

'''
1번 회사에서 출발해 K번 회사를 방문한 다음,
X번 회사에 가서 커피를 마신다. 빠르게 이동하는 경로는?
'''

import sys
inputF = sys.stdin.readline

# N=회사, M=경로
N, M = map(int, inputF().split())
INF = int(1e9)

# 플로이드워셜 적용을 위한 2차원 그래프
graph = [[INF] * (N+1) for _ in range(N+1)]


# 자기 자신에 대한 경로는 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0


for _ in range(M):
    a, b = map(int, inputF().split())
    graph[a][b] = 1  # 최근접이기 때문에 1
    graph[b][a] = 1

# X=도착치, K=경유지
X, K = map(int, inputF().split())


# 알고리즘 (Floyd-Warshall)
for k in range(1, N+1):
    for a in range(1, N+1):
        for b in range(1, N+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

# 1번에서 X를 경유해 K까지 간 거리
distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print(-1)
else:
    print(distance)


'''
입력 예시
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

결과 = 3
'''