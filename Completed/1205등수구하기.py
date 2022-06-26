# 백준 1205 등수 구하기 실버 5
'''
랭킹 리스트가 100, 90, 90, 80일 때 각각의 등수는 1, 2, 2, 4등이 된다.

랭킹 리스트에 올라 갈 수 있는 점수의 개수 P
리스트에 있는 점수 N개

태수의 새로운 점수가 주어진다. 
태수의 새로운 점수가 랭킹 리스트에서 몇 등 하는지 구하는 프로그램을 작성하시오. 
만약 점수가 랭킹 리스트에 올라갈 수 없을 정도로 낮다면 -1을 출력한다.

랭킹 리스트가 꽉 차있을 때, 
새 점수가 이전 점수보다 더 좋을 때만 점수가 바뀐다.

'''
import sys
inputF = sys.stdin.readline
N, score, P = map(int, inputF().split())

if N == 0:
    print('1')
    sys.exit(0)
else:
    NList = list(map(int, inputF().split()))
    if N == P and NList[-1] >= score:
         print('-1')
    else:
        for idx, rank in enumerate(NList):
            if score >= rank:
                print(idx+1) 
                sys.exit(0)
        if score not in NList:
            print(len(NList)+1)

