# 문제 원문 https://community.topcoder.com/stat?c=problem_statement&pm=10297
# 백준 1004  어린왕자
# 기하학
'''
핵심 - 최소의 원을 지날 수 있는 경우를 계산.
그림을 보니까 어쩔 수 없이 뚫고 지나가야 하는 경우만 계산하면 되는 듯.

행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다.
또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.

입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다.
두 번째 줄에는 행성계의 개수 n이 주어지며,
세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.

2 <- 테스트 케이스
-5 1 12 1   <- x1, y1, x2, y2
7           <- 행성계 개수
1 1 8       <- 여기부터 cx, cy, r
-3 -1 1
2 2 2
5 5 1
-4 5 1
12 1 1
12 1 2
'''
import sys
from math import sqrt  # 제곱근 함수, "** 0.5"로 계산해도 동일 결과
inputF = sys.stdin.readline
T = int(inputF())
for _ in range(T):
    x1, y1, x2, y2 = map(int, inputF().split())
    pT = int(inputF())
    result = 0  # 통과하는 행성 수
    for _ in range(pT):
        cx, cy, r = map(int, inputF().split())

        # 출발지, 목적지가 같은 행성 안에 포함되는지 파악. (해당 경우는 1 더할 필요가 없기 때문)
        if sqrt((x1-cx)**2 + (y1-cy)**2) < r:
            if sqrt((x2-cx)**2 + (y2-cy)**2) < r:
                pass
            else:
                # 출발지, 목적지가 같은 행성 내에 없으면
                result += 1
        elif sqrt((x2-cx)**2 + (y2-cy)**2) < r:
            result += 1
    print(result)

    t=0
    for c in l:

        A = 1 if sqrt((x1-cx)**2 + (y1-cy)**2) < r else 0
        B = 1 if sqrt((x2-cx)**2 + (y2-cy)**2) < r else 0
        if  A^B==1: result+=1    # XOR 연산으로 행성 통과 유무 계산


'''
테스트 케이스
1
-3 2 0 0
6
0 0 9
2 1 5
-3 -3 2
-1 0 11
1 1 3
9 8 9    -> 2 
'''

'''
다른 인원 문제 풀이 (XOR 사용)
XOR은 두 비교가 다른 값일 때 (1, 0) 또는 (0, 1) True를 반환한다.
조건에서 보면 출발지, 도착지 두 점이 모두 같은 행성 안에 있으면 (1, 1) 오히려 반영하지 않는다.
둘 중 하나의 점만 행성 안에 포함되어 있어야 반영하는 구조인 것이다. (1,0), (0,1)일 때.
그래서 XOR을 사용하며 이를 통해 조건문 하나를 없앨 수 있다.

import sys;read=sys.stdin.readline
for T in range(int(read())):
    x1,y1,x2,y2=map(int,read().split())
    n=int(read())
    l=[list(map(int,read().split()))for i in range(n)]
    t=0
    for c in l:
        A = 1 if (x1-c[0])**2+(y1-c[1])**2 < c[2]**2 else 0
        B = 1 if (x2-c[0])**2+(y2-c[1])**2 < c[2]**2 else 0
        if  A^B==1:t+=1
    print(t)
'''