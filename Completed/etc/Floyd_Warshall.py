# 최단 경로 알고리즘

# Floyd-Warshall Algorithm
'''
모든 지점에서 다른 모든 지점의 노드의 최단 거리를 계산하는 알고리즘
2차원 리스트로 구성되며 단계마다 N^2의 시간 복잡도를 가짐
-> 전체적으로 N^3의 시간 복잡도
'''

'''
1 ---4--- 2
1 ---6--- 4
2 ---3--- 1
2 ---7--- 3 
3 ---5--- 1
3 ---4--- 4
4 ---2--- 3
'''
import sys
inputF = sys.stdin.readline
INF = int(1e9) #INFINITY

N, M = map(int, inputF().split())
graph = [[INF] * (N+1) for _ in range(N+1)] # 2차원 리스트로 그래프

# 자기 자신에 대한 노드는 0으로 처리
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j: graph[i][j] = 0

# 각 노드에 대한 간선 정보 입력 받으면 그래프 갱신
for _ in range(M):
    sn, dn, dist = map(int, inputF().split())
    graph[sn][dn] = dist


# Algorithm
for k in range(1, N+1): # 경유지
    for a in range(1, N+1): # 출발지
        for b in range(1, N+1): # 목적지
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])



# 처리 결과 출력
for a in range(1, N+1):
    for b in range(1, N+1):
        if graph[a][b] == INF:
            print("INF")
        else:
            print(graph[a][b], end=' ')
    print()


'''
사용 예시

4 7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력

0 4 8 6  
3 0 7 9  
5 9 0 4  
7 11 2 0
'''