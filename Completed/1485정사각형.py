# 백준 1485 정사각형 문제

'''
네 점이 주어졌을 때, 
네 점을 이용해 정사각형을 만들 수 있는지 없는지를 구하는 프로그램을 작성하시오.

'''

'''
4변의 길이가 모두 일치하는지 확인.
2개의 대각의 길이가 모두 일치하는지 확인. 

-> 정사각형이 되기 위한 명제를 달성하는 과제임.
'''

import sys
case = int(input())
arrL = []
ret = []

def Check_Square(Arr : list):
    LineList = []
    Arr = sorted(Arr)
    LineList.append((abs(Arr[0][0] - Arr[1][0]) + abs(Arr[0][1] - Arr[1][1]))) # a-b 길이
    LineList.append((abs(Arr[0][0] - Arr[2][0]) + abs(Arr[0][1] - Arr[2][1]))) # a-c 길이
    LineList.append((abs(Arr[3][0] - Arr[1][0]) + abs(Arr[3][1] - Arr[1][1]))) # b-d 길이
    LineList.append((abs(Arr[3][0] - Arr[2][0]) + abs(Arr[3][1] - Arr[2][1]))) # c-d 길이
        
    diagonal1 = (abs(Arr[1][0] - Arr[2][0]) + abs(Arr[1][1] - Arr[2][1])) # b-c 길이 (대각1)
    diagonal2 = (abs(Arr[0][0] - Arr[3][0]) + abs(Arr[0][1] - Arr[3][1])) # a-d 길이 (대각2)
    #print(f"{LineList=}, {diagonal=}")
        
    if len(set(LineList)) == 1 and diagonal1 == diagonal2 :
        return 1
    else:
        return 0


for i in range(1, case*4+2 + (case-1)):
    if i%5 == 0:
        # 정사각형 판별 함수
        ret.append(Check_Square(arrL))
        arrL.clear()
    else:
        arrL.append(list(map(int, sys.stdin.readline().split())))

for i in ret:
    print(i)