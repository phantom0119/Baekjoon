# 그래프 이론, 위상정렬 (Topology Sort)
'''
순서가 정해진 (방향성이 있는) 일련의 작업을 차례대로 수행하는 과정을 설명.
-> 방향 그래프의 모든 노드를 방향성에 거스르지 않고 순서대로 정렬하는 것.

'시작점'이 반드시 필요하기 때문에 그래프는 Cycle 성질을 가지지 않아야 한다.
-> Cycle 성질이 있으면 시작을 어디서 하든 상관 없어지기 때문이다.

시작점은 '진입차수'가 0인 것을 선택해야 한다. (자신에게 들어오는 간선이 없는 노드)

1. 진입차수가 0인 노드를 Queue에 추가.
2. Queue가 소진될 때까지 과정 반복.
  -> Queue에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거.
  -> 위의 결과에서 새롭게 진입차수가 0이 된 노드를 Queue에 추가.

※ 노드 개수가 V일 때, Queue에서 처리한 원소의 개수가 V가 되기 전에 비어버리면
   Cycle이 형성된 그래프임을 알아낼 수 있다.

  
노드와 간선을 하나씩 모두 탐색하기 때문에 시간 복잡도는 O( V+E )
'''

import sys
from collections import deque
inputF = sys.stdin.readline

# V=노드, E=간선
V, E = map(int, inputF().split())

# 진입 차수
indegree = [0] * (V+1)

# 각 노드의 간선 정보 graph
graph = [[] for _ in range(V+1)]


# 입력 받은 간선 정보에 따른 처리
for _ in range(E):
  a, b = map(int, inputF().split())
  graph[a].append(b)
  indegree[b] += 1


def topology_sort():
  ret = []  # 위상정렬 결과
  q = deque()

    # 진입 차수가 0인 노드를 찾아 Queue에 추가
  for i in range(1, V+1):
    if indegree[i] == 0:
      q.append(i)
    

  # Queue가 빌 때까지 반복
  while q:
    tmp = q.popleft()
    ret.append(tmp)
    
    # tmp 노드와 연결된 간선 제거 (1씩 빼기)
    for i in graph[tmp]:
      indegree[i] -= 1

      # 뺀 결과로 진입 차수가 0이 되면 Queue에 추가
      if indegree[i] == 0:
        q.append(i)

  for i in ret:
    print(i, end=' ')


topology_sort()


'''
입력 예시

7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
-> 1 2 5 3 6 4 7
'''