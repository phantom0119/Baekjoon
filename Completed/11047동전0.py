# 백준 11047   동전0    실버4
# 그리디 알고리즘
from sys import stdin
inputF = stdin.readline

N, K = map(int, inputF().split())
Money = []
for _ in range(N): Money.append(int(inputF()))

Money.sort(reverse=True)
cnt = 0
for M in Money:
    if M > K: pass
    else:
        cnt += K//M
        K = K%M
        #print(f"{cnt=},  {K=}")

print(cnt)