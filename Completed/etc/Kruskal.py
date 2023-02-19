# 그래프 이론, 그리디.
# 서로소 집합을 활용한 크루스칼 알고리즘
'''
최소의 비용으로 신장 트리 (Spanning Tree)를 찾아야 할 경우 적용.
= 최소 신장 트리 알고리즘

1. 간선 데이터를 비용(거리)에 따라 오름차순 정렬.
2. 간선을 확인하며 현재의 간선이 사이클을 형성하는지 확인 (신장 트리 특징).
   2-1: 사이클이 발생하지 않는다면 최소 신장 트리에 포함.
   2-2: 사이클이 발생하면 제외.
3. 모든 간선에 대해 2번 계속.

이름에서 확인하면 Tree임을 알 수 있다.
그래서 최종으로 구성된 간선 E는 노드 개수가 V일 때 V-1의 값을 가진다.
E = V-1

'''
import sys
inputF = sys.stdin.readline

# Disjoint Set (Union-Find)
def find_parent(parent, x):
    # 부모가 자기 자신이 아니라면 상위 부모 찾기
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 노드 번호가 작으면 우선한다고 가정
    if a < b:    
        parent[b] = a
    else:
        parent[a] = b


def kruskal(edges : list):
    # 비용(거리) 저장
    distance = 0
    parent = [0] * (V+1)

    # 초기화: 자기 자신을 부모로
    for i in range(1, V+1):
        parent[i] = i

    for edge in edges:
        # 튜플 정보 대입
        cost, a, b = edge

        # a의 부모와 b의 부모가 같지 않다 = Cycle이 아니다
        if find_parent(parent, a) != find_parent(parent, b):
            
            # 부모 정보를 갱신 후 비용(거리) 계산 
            union_parent(parent, a, b)
            distance += cost
    
    return(distance)


if __name__ == '__main__':
    # 노드, 간선 개수 
    V, E = map(int, inputF().split())

    # 간선 정보
    edges = []
    
    for _ in range(E):
        # 간선 정보 입력 받기
        a, b, cost = map(int, inputF().split())
        edges.append((cost, a, b))

    # 거리(cost)를 기준으로 오름차순 정렬
    edges.sort()

    print(kruskal(edges)) 


'''
입력 예시

7 9
1 2 29
1 5 75
2 3 35
2 6 34
3 4 7
4 6 23
4 7 13
5 6 53
6 7 25

결과 = 159
'''