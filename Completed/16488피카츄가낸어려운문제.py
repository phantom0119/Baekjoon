# 백준  16488  피카츄가 낸 어려운 문제    실버5
# 수학, 기하학

'''
이등변삼각형 ABC에서 변 BC 위에 점 P1, P2, ··· , PK을 잡는다.

i = 1, 2, ··· , K에 대하여 
함수 F(i)를 
(선분 APi의 길이)² + (선분 BPi의 길이) x (선분 CPi의 길이)로 정의한다.

이때, F(1)+F(2)+···+F(K)의 값은 얼마인지 구하시오.
'''
import sys
from math import floor
N, K = map(int, sys.stdin.readline().split())

# 선분 BC의 길이
BC = N * (2**0.5)
# 이등변을 K등분 한 선분 1개 길이
Ak = N/(K+1)
# K등분 선분 1개 길이
pk = BC / (K+1)
#print(f"{BC=}, {Ak=}, {pk=}")
ret = []

AP = (1**2 + (K)**2) **0.5 * Ak
print(floor((AP**2 + K*pk**2) * K))


'''
for i in range(1, K+1):
    AP = (i**2 + (K+1-i)**2) **0.5 * Ak
    BP = pk*i
    CP = pk*(K+1-i)
    print(f"{AP=}, {BP=}, {CP=}")
    ret.append(AP**2 + BP * CP)

print(ret)
print(floor(sum(ret)))
'''


'''
# 천재..

n,k = map(int,input().split())
print(n*n*k)

'''