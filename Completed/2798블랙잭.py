# 백준 2798 블랙잭 브론즈2
'''
N장의 카드 중에서 3장의 카드를 골라야 한다. 
플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때, 
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.


첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다. 
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 
이 값은 100,000을 넘지 않는 양의 정수이다.
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.

첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
'''
import sys
inputF = sys.stdin.readline

def comb(lis, n):
    result = []
    if n > len(lis):
        return result

    if n == 1:
        for i in lis:
            result.append([i])
    elif n > 1 :
        for i in range(len(lis) - n + 1):
            for j in comb(lis[i+1 :], n-1):
                result.append([lis[i]] +j)
    
    return result

N, M = map(int, inputF().split())
Cards = list(map(int, inputF().split()))
Cards_Sum = comb(Cards, 3)

ret = []
for Card in Cards_Sum:
    if sum(Card) - M > 0:
        pass
    else:
        ret.append([abs(sum(Card)-M), sum(Card)])

print(min(ret[0:])[1])




'''
def blk(a, b) :
    a = sorted(a)
    answer = 0
    for i in range(len(a)) :
        for ii in range(i+1, len(a)) :
            for iii in range(ii+1, len(a)) :
                tmp = a[i] + a[ii] + a[iii]
                if tmp > b :
                    break
                elif tmp == b :
                    return b
                elif tmp > answer :
                    answer = tmp
                
    return answer

a, b = map(int, input().split())
a = list(map(int, input().split()))
print(blk(a, b))
'''

'''
N, M = map(int, input().split())
cards = list(map(int, input().split()))

current = 0
for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            tmp = cards[i]+cards[j]+cards[k]
            if current < tmp <= M:
                current = tmp

print(current)
'''