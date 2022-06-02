# 참고 : https://ourcalc.com/%EC%A1%B0%ED%95%A9-%EA%B3%84%EC%82%B0%EA%B8%B0/    (조합 계산식)
# https://ourcalc.com/%EC%88%9C%EC%97%B4-%EA%B3%84%EC%82%B0%EA%B8%B0/     (순열 계산식)
# 백준 1010 다리놓기
# 조합론, 수학, 다이나믹 프로그래밍
'''
강 주변에서 다리를 짓기에 적합한 곳을 사이트라고 한다.
재원이는 강 주변을 면밀히 조사해 본 결과,
강의 서쪽에는 N개의 사이트가 있고 동쪽에는 M개의 사이트가 있다는 것을 알았다. (N ≤ M)

서쪽의 사이트 개수만큼 (N개) 다리를 지으려고 한다.
다리끼리는 서로 겹쳐질 수 없다고 할 때 다리를 지을 수 있는 경우의 수를 구하는 프로그램을 작성하라.
'''
import sys
from math import factorial
inputF = sys.stdin.readline
T = int(inputF())
for _ in range(T):
    N, M = map(int, inputF().split())
    ''' 조합 계산식 변형.  nCr = nPr / r! '''
    mPn = factorial(M) // factorial(M-N)
    nFacto = factorial(N)
    print(mPn//nFacto)