# 백준 10816 숫자카드2 실버4
'''
상근이는 숫자 카드 N개를 가지고 있다. 
정수 M개가 주어졌을 때, 
이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하셈.
'''
import sys
inputF = sys.stdin.readline
A_cnt = int(inputF())
A_Cards = list(map(int, inputF().split()))
B_cnt = int(inputF())
B_Cards = list(map(int, inputF().split()))
Cards_dict = dict()

# for card in set(A_Cards):
#     Cards_dict[card] = A_Cards.count(card)
for card in A_Cards:
    if card in Cards_dict:
        Cards_dict[card] += 1
    else:
        Cards_dict[card] = 1

for Card in B_Cards:
    try:
        print(Cards_dict[Card], end=' ')
    except KeyError:
        print('0', end=' ')



'''
n = int(input())
dic = {}

for i in map(int, input().split()):
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

m = int(input())
answer = []
for j in map(int, input().split()):
    if j in dic:
        answer.append(dic[j])
    else:
        answer.append(0)

print(' '.join(map(str, answer)))
'''

'''
from sys import stdin
_ = stdin.readline()
n = map(int,stdin.readline().split())
_ = stdin.readline()
m = map(int,stdin.readline().split())
hashmap = {}


for i in n:
    if i in hashmap:
        hashmap[i] += 1
    else:
        hashmap[i] = 1

print(' '.join(str(hashmap[i]) if i in hashmap else '0' for i in m))

'''