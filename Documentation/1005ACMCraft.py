# 백준 1005 ACM Craft
# 그래프이론, 다이나믹 프로그래밍, 위상 정렬
'''
위상정렬 : 순서가 정해진 작업을 차례로 수행할 때 그 순서를 결정하기 위한 알고리즘
         여러 답이 존재할 수 있으며 사이클이 발생하지 않는 방향 그래프이다.

큐 활용 (진입 차수)
진입 차수가 0인 정점을 큐에 추가 (첫 시작하는 값)   ->  1
큐에서 원소(첫 값)을 꺼내 제거 (연결된 간선 제거)
이후에 진입 차수가 0이 되는 값을 큐에 추가         ->  2, 3
큐가 비어질 때까지 해당 과정 반복

위상 정렬 알고리즘 설명 = https://m.blog.naver.com/ndb796/221236874984
질문 참고 : https://www.acmicpc.net/board/view/77853
'''
# N = 건물의 개수
# K = 건설순서 규칙 총 개수
import sys
from collections import deque  # Queue 함수를 사용하기 위한 데큐
inputF = sys.stdin.readline
T = int(inputF())
Build_Time = dict()  # 건설 시간 저장 딕셔너리
tmp = 0  # 건설 시간 저장하는 임시 변수

def Topology_Sort():  # 위상정렬 알고리즘
    q = deque()       # Deque 객체

    '''진입 차수가 0인 건물을 찾는다.
    처음 짓기 시작한 건물은 첫 입력에 진입 차수가 0일 것이다.
    건물을 짓기 위해 소요되는 시간은 'time' 리스트에 누적한다.
    그리고, q에 해당 건물 번호를 추가한다.'''
    for i in range(1, N+1):   # 진입 차수가 0인 건물을 찾아서 건설 시간 저장
        if indegree[i] == 0:
            time[i] = Build_Time[i]
            q.append(i)

    '''q에 데이터가 있다는 것은 아직 목표 건물까지 도달하지 않았음을 의미.
       목표 건물까지 도달하는 과정을 q를 통해 조절'''
    while q:
        value = q.popleft()  # 첫 1 추출
        tmp = time[value]    # 추출된 건물에 대한 건설 시간

        for i in Rule[value]: # 해당 건물 다음으로 건설하는 건물 차수 1 빼기.
            # 진입 차수가 2개 이상인 경우는 이전 값과 비교해 큰 값으로 대체.
            time[i] = max(time[i], tmp + Build_Time[i])  # 해당 건물까지의 건설 최대 소요 시간.
            indegree[i] -= 1  # 진입 차수 1 차감.

            if indegree[i] == 0:  # 집입 차수가 0이 되면 추가.
                q.append(i)

for _ in range(T):
    N, K = map(int, inputF().split())  # 건물 개수 N, 규칙 개수 K
    Values = list(map(int, inputF().split()))  # 건물 건설 시간 리스트
    indegree = [0] * (N+1) # 각 건물의 진입 차수 리스트
    time = [0] * (N+1)     # 각 건물의 건설 시간 (추후 누적)
    Rule = [[] for _ in range(N+1)] # 건물 규칙 정보 저장 리스트


    for i in range(1, N+1): # 각 건물에 대한 시간 딕셔너리
        Build_Time[i] = Values[i-1]

    for i in range(K): # 간선 규칙 정보 담기
        outV, inV = map(int, inputF().split())
        # 뻗어 나가는 가지가 2개 이상일 경우 처리 방법
        Rule[outV].append(inV)  # 좌측(outV 완료한 건물) 우측(inV 다음 건물)
        # 들어온 가지 수는 곧 진입 차수를 의미.
        indegree[inV] += 1  # 진입 차수 1 증가

    W = int(inputF())
    Topology_Sort()
    print(time[W])



'''
다른 사람 문제 풀이 1

import sys
from collections import deque, defaultdict

sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(w):
  if dp[w] == -1:
    dp[w] = 0
    for adj in prev[w]:
      dp[w] = max(dp[w], dfs(adj))
    dp[w] += time[w]
  return dp[w]
  
if __name__ == '__main__':
  for _ in range(int(input().strip())):
    n, k = map(int, input().strip().split())
    time = [0]+list(map(int, input().strip().split()))
    
    prev = [[] for _ in range(n+1)]
    for _ in range(k):
      a, b = map(int, input().strip().split())
      prev[b].append(a)
    
    w = int(input().strip())
    dp = [-1]*(n+1)
    print(dfs(w))
'''

'''
다른 사람 문제 풀이 2
-> 재귀를 사용하는 경우 
import sys
sys.setrecursionlimit(10 ** 6)

= [만약 재귀를 사용해서 풀어야 하는 문제라면, 위 코드를 상단에 쓰는 것은 선택이 아닌 필수이다. 
파이썬의 기본 재귀 깊이 제한은 1000으로 매우 얕은 편이다. 
따라서 재귀로 문제를 풀 경우 드물지 않게 이 제한에 걸리게 되는데, 
문제는 코딩테스트 환경에서는 에러 메시지를 볼 수 없다는 것이다. 
이 함정에 걸린 사람은 원인 미상의 런타임 에러를 붙잡고 몇십 분을 각종 테스트케이스를 넣어가며 씨름하겠지만, 
그런다고 문제가 잡힐 리 없다. 
결국에는 문제를 풀지 못한 채 제출하게 되고 내가 뭘 잘못했지 하는 끝없는 자괴감에 빠지게 되는 것이다.]

from sys import stdin, setrecursionlimit as SRL
SRL(1_000_000)

input = stdin.readline

def solve():
    def dfs(cur):
        if dp[cur] != -1:
            return dp[cur]

        t = max([dp[i] if dp[i] != -1 else dfs(i) for i in indegree[cur]], default=0)
        dp[cur] = t + time[cur]
        return dp[cur]

    for _ in range(int(input())):
        N, K = map(int, input().split())
        time = [0, *map(int, input().split())]
        indegree = [[] for _ in range(N + 1)]
        for _ in range(K):
            before, after = map(int, input().split())
            indegree[after].append(before)

        W = int(input())
        dp = [-1] * (N + 1)
        print(dfs(W))


if __name__ == '__main__':
    solve()

'''