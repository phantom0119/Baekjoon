# 백준 25325  학생 인기도 측정   실버5
# 문자열, 정렬, 트리 집합과 맵
from sys import stdin
inputF = stdin.readline
cnt = int(inputF())
Member = dict()

MList = list(inputF().split())

for m in MList:
    Member[m] = 0

#print(Member)
for _ in range(cnt):
    MString = list(inputF().split())
    for m in MString:
        Member[m] += 1

Member = list(zip(Member.keys(), Member.values()))
Member.sort(key=lambda x: x[1], reverse=True)

for i in Member:
    print(f"{i[0]} {i[1]}")