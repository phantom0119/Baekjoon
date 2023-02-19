# 최단 경로 문제

# Dijkstra algorithm
'''
한 노드를 시작점으로 고정하고,
그래프의 다른 모든 꼭짓점까지의 최단경로를 찾는 알고리즘으로 최단 경로 트리를 만듦.

Python에서 우선순위 큐(Priority Queue)를 이용해서 구현하면 전체 N*logN 복잡도로 처리 가능.


시작노드 1.    전체 노드 6.

1 -----2---->  2
1 -----5---->  3
1 -----1---->  4
2 -----3---->  3
2 -----2---->  4
3 -----5---->  6
4 -----3---->  3
4 -----1---->  5
5 -----1---->  3
5------2---->  6
'''
import heapq  # 우선순위 큐 (Heap) 사용
import sys
inputF = sys.stdin.readline
INF = int(1e9)  # 최단 갱신이 안 된 노드에 무한값 적용 (10억)

# Algorithm
def dijkstra(start):
    q = []  # Heap으로 사용
    heapq.heappush(q, (0, start)) # 시작노드, 0 = 최단거리
    distance[start] = 0

    while q:
        #우선순위 높은 노드 정보 추출
        dist, node = heapq.heappop(q)  
        

        # 최단 경로 갱신을 마친 경우엔 통과
        if distance[node] < dist:  
            continue
        
        # 선택된 노드와 인접한 노드의 최단 경로 갱신
        for i in graph[node]: 
            cost = dist + i[1]

            # 최단경로 갱신이 필요하다면
            if cost < distance[i[0]] : 
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


if __name__ == '__main__':
    #N = 6 # 노드 개수
    N = int(inputF())

    #M = 11 # 간선 개수
    M = int(inputF())

    start = int(inputF()) # Start Node

    distance = [INF] * (N+1)  #각 노드에 도달하는 최단 거리
    graph = [ [] for _ in range(N+1) ] # 노드 그래프

    # 간선 정보 입력
    for _ in range(M):
        # sn = 출발노드,  dn = 목적지노드,  dist = 거리
        sn, dn, dist = map(int, inputF().split())
        graph[sn].append((dn, dist))
    
    dijkstra(start)

    for i in range(1, N+1):
        if distance[i] == INF:
            print('INF')
        else:
            print(distance[i])
        
'''
6
11
1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
'''