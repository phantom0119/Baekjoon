# 백준 25814   등가수열 구하기    실버4
# 구성적
'''
길이가 N인 동가수열은 다음 두 조건을 만족하는 수열이다.

동가수열은 1 이상 N 이하인 정수로 이루어져 있고, 모든 원소는 서로 다르다.
동가수열의 서로 이웃한 원소의 차는 [N/2]이상이다.


[N/2]는 N/2보다 크지 않은 정수 중 가장 큰 정수를 의미
3.7 = 3,   4 = 4 (floor 내림 개념)


길이가 N인 동가수열을 아무거나 하나 구해보자. 
주어지는 모든 입력에 대해 동가수열은 항상 존재한다.
'''
from sys import stdin
#from math import floor
N = int(stdin.readline())
tmp = rnd = N//2
ret = []
cnt = 0

if N == 1: print(1); exit()

while True:
    if cnt == N: break

    if cnt == 0 :
        ret.append(rnd)
        cnt += 1
    else:
        if tmp + rnd > N:
            n = 0
            while True:
                if tmp - (rnd+n) not in ret:
                    tmp = tmp - (rnd+n)
                    ret.append(tmp)
                    cnt += 1
                    break
                else:
                    n += 1
        else:
            n = 0
            while True:
                if tmp + (rnd+n) not in ret:
                    tmp = tmp + (rnd+n)
                    ret.append(tmp)
                    cnt += 1
                    break
                else:
                    n += 1

print(*ret)

'''
6이라면,  3,   3 - 6 - 2 - 5 - 1 - 4
'''


'''
# 연구잼

n = int(input())
x = n // 2

value = x + n % 2
ans = [value]

for i in range(n - 1):
    if i % 2 == 0:
        value += x
        ans.append(value)
    else:
        value -= x + 1
        ans.append(value)

print(*ans)

'''