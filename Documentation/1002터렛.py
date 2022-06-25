# 백준 1002 터렛
# 원의 내적, 외적에 대한 판단 문제
'''
조규현의 좌표 (x1, y1)와 백승환의 좌표 (x2, y2)가 주어지고,
조규현이 계산한 류재명과의 거리 r1과 백승환이 계산한 류재명과의 거리 r2가 주어졌을 때,
류재명이 있을 수 있는 좌표의 수를 출력하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.
한 줄에 x1, y1, r1, x2, y2, r2가 주어진다.
x1, y1, x2, y2는 -10,000보다 크거나 같고, 10,000보다 작거나 같은 정수이고,
r1, r2는 10,000보다 작거나 같은 자연수이다.

만약 류재명이 있을 수 있는 위치의 개수가 무한대일 경우에는 -1을 출력한다.

3
0 0 13 40 0 37     ->   2
0 0 3 0 7 4             1
1 1 1 1 1 5             0
'''
import sys
from math import sqrt  # sqrt : 제곱근 함수
inputF = sys.stdin.readline # 입력 명령 문자열 간소화

def TestFunction(TList : list):
    # d = 두 점의 거리
    d = sqrt((TList[0] - TList[3])**2 + (TList[1] - TList[4])**2)

    '''
    경우 1 : 동심원 (두 점의 위치가 같고(d=0) 거리(r1,r2)도 서로 같다.  => 무한대(-1)
    경우 2 : 만나지 않음(0) = d가 두 반지름보다 길다 = 두 원이 떨어짐.
                            d가 두 반지름의 차보다 작다 = 하나의 원은 다른 원 안에 존재.
    경우 3 : 1개의 점에서 만남(1) = d가 두 반지름의 거리 합과 같다. (외접)
                                 d가 두 반지름의 거리 차와 같다. (내접)
    경우 4 : 일반적인 경우(2) = 위의 특이 경우에 해당하지 않으면 두 점과 만남.
    '''

    if d == 0 and TList[2] == TList[5]:  # Figure 4
        return -1
    elif d > TList[2]+TList[5] or d < abs(TList[2]-TList[5]): # Figure 1
        return 0
    elif d == TList[2]+TList[5] or d == abs(TList[2]-TList[5]): # Figure 2
        return 1
    else:  # Figure 3
        return 2

if __name__ == '__main__':
    T = int(inputF()) # TestCase Count

    for _ in range(T):
        TestList = list(map(int, inputF().split()))
        print(TestFunction(TestList))  # 구현 함수


