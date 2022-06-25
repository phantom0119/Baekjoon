# 백준 1011 Fly me to the Alpha Centauri
# 수학
'''
이전 작동시기에 k광년을 이동하였을 때는 k-1 , k 혹은 k+1 광년만을 다시 이동할 수 있다.
예를 들어, 이 장치를 처음 작동시킬 경우 -1 , 0 , 1 광년을 이론상 이동할 수 있으나
사실상 음수 혹은 0 거리만큼의 이동은 의미가 없으므로 1 광년을 이동할 수 있으며,

그 다음에는 0 , 1 , 2 광년을 이동할 수 있는 것이다.
( 여기서 다시 2광년을 이동한다면 다음 시기엔 1, 2, 3 광년을 이동할 수 있다. )

x지점에서 y지점을 향해 최소한의 작동 횟수로 이동하려 한다.
y지점에 도착해서도 공간 이동장치의 안전성을 위하여 y지점에 도착하기 바로 직전의 이동거리는 반드시 1광년으로 하려 한다.

 x지점부터 정확히 y지점으로 이동하는데 필요한 공간 이동 장치 작동 횟수의 최솟값을 구하는 프로그램을 작성하라.
'''
import sys
from math import sqrt   # ** 0.5 계산으로 적용 가능
inputF = sys.stdin.readline
dist = []
t = int(inputF())

for _ in range(t):
    num1, num2 = map(int, inputF().split())
    dist.append(num2 - num1)

for dis in dist:  # 각각의 테스트 케이스 한 번에 처리
    y = int(sqrt(dis))
    z = y + 1

    if y == 1:  # 규칙1 : 제곱근이 1이면 (거리만큼 출력)
        print(dis)
    elif dis >= y * z + 1:   # 규칙2 : 거리가 N*(N+1)+1 이상일 때 (같은 제곱근 범위 안)
        print(y + z)
    elif dis >= y ** 2 + 1:  # 규칙3 : 거리가 N^2+1 이상일 때 (새로운 제곱근 범위)
        print(y * 2)
    else:
        print(y * 2 - 1)

