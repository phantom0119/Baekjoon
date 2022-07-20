#  백준  10815  숫자카드   실버5
# 이분탐색, 정렬, 자료구조
import sys
inputF = sys.stdin.readline
cnt = int(inputF()) # 가지고 있는 카드
CardDict = dict()

M = list(map(int, inputF().split()))
for i in M:
    try:
        CardDict[i] += 1
    except KeyError:
        CardDict[i] = 1

cnt = int(inputF())  # 물어본 카드
Result = [0] * cnt
M = list(map(int, inputF().split()))
for idx, i in enumerate(M):
    try:
        Result[idx] = CardDict[i]
    except KeyError:
        continue

#print(' '.join(str(i) for i in Result))
print(*Result)



'''
# 딕셔너리를 이렇게 사용합시다.

def solution(n, list1, m, list2):
    hash = {};
    for num in list1:
        hash[num] = 1

    for idx in range(len(list2)):
        list2[idx] = hash.get(list2[idx], 0)

    print(*list2)

n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
solution(n, list1, m, list2)

'''