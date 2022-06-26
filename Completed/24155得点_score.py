#백준 24155번 : 得点 (Score) 다국어
'''
요 전날 JOI 대학 정보 학과에서 입학 시험을 실시했습니다. 
시험은 100점 만점이었고, n명의 학생이 수험했다. 
JOI 대학에서는 합격 최저점을 결정하기 위해 시험 결과를 바탕으로 각 학생에게 순위를 매기기로 했다.

n 학생의 점수가 주어지면 각 학생의 순위를 결정하는 프로그램을 작성하십시오. 
그러나 같은 점수를 가진 학생이있을 수 있습니다.

입력의 첫 번째 줄에는 학생 수 n (1 ≤ n ≤ 100000)이 있습니다. 
다음 n 행은 학생의 점수를 나타냅니다. 
i + 1 (1 ≤ i ≤ n) 라인에는 시험 번호 i의 학생 점수 si (0 ≤ si ≤ 100)가 기록됩니다.
'''


import sys
from collections import Counter

cnt = int(sys.stdin.readline())
score = []
rank_dict = {}
for i in range(cnt):
    score.append(int(sys.stdin.readline()))

Values = Counter(score)
score_set = sorted(set(score), reverse=True)

n = 0
for rank, scr in enumerate(score_set):
    rank_dict[scr] = rank +1 +n

    if Values[scr] > 1:
        n = n + Values[scr] -1

for scr in score:
    print(rank_dict[scr])