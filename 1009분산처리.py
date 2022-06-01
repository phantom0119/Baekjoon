# 백준 1009 분산처리
# 수학, 구현
'''
각 컴퓨터에 1번부터 10번까지의 번호를 부여하고, 10대의 컴퓨터가 다음과 같은 방법으로 데이터들을 처리하기로 하였다.
1번 데이터는 1번 컴퓨터, 2번 데이터는 2번 컴퓨터, 3번 데이터는 3번 컴퓨터, ... ,
10번 데이터는 10번 컴퓨터, 11번 데이터는 1번 컴퓨터, 12번 데이터는 2번 컴퓨터, ...

총 데이터의 개수는 항상 ab개의 형태로 주어진다.
재용이는 문득 마지막 데이터가 처리될 컴퓨터의 번호가 궁금해졌다.
이를 수행해주는 프로그램을 작성하라.
'''
import sys
inputF = sys.stdin.readline
N = int(inputF())
for i in range(N):
    a, b = map(int, inputF().split())

    rules = []
    n = 1
    while True:   # 나머지 규칙 찾아냄 (계산 과정 줄이기)
        if a**n%10 in rules:
            break
        else:
            rules.append(a**n%10)
            n += 1

    b = b%len(rules)    # 나머지 규칙 개수로 지수 계산 삭제
    if rules[b-1] == 0: # 나머지 0이 나오는 경우 = 10 번째 PC
        print('10')
    else:
        print(rules[b-1])
