# 1037 약수 문제
# 수학, 정수론

'''
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

첫째 줄에 N의 진짜 약수의 개수가 주어진다. 
이 개수는 50보다 작거나 같은 자연수이다. 
둘째 줄에는 N의 진짜 약수가 주어진다. 
1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

2
4 2   ->   8

1
2    ->    4

'''
import sys
cnt = int(input())
values = list(map(int, sys.stdin.readline().split()))
#Max_V = max(values)
Comp_Val = max(values)*2

#print(f"{values=}, {Comp_Val}")

for i in range(2, Comp_Val+1):
    if Comp_Val % i == 0:
        if i not in values:
            Max_V = max(values) * min(values)
            print(Max_V)
            break
    else:
       print(Comp_Val)
       break


'''
브론즈 5  2338 긴자리 계산

A = int(input())
B = int(input())
print(f"{A+B}\n{A-B}\n{A*B}")

'''

'''
브론즈 5 2845 파티가 끝나고 난 뒤


import sys
x, y = map(int, sys.stdin.readline().split())
vList = list(map(int, sys.stdin.readline().split()))
ret = []

size = x*y
for i in range(len(vList)):
    print(vList[i]-size, end= ' ')

'''

'''
브론즈5 2914 저작권

창영이는 자신의 앨범에 포함되어있는 저작권이 있는 멜로디의 평균값을 구해보기로 했다. 
이 값은 아래와 같이 구할 수 있다.

(저작권이 있는 멜로디의 개수) / (앨범에 수록된 곡의 개수)

이때, 평균값은 항상 올림을 해서 정수로 만들어야 한다.
예를 들어, 창영이의 1집 앨범 "영창에서 영원히 영창피아노를 친다"에
총 38개 곡이 수록되어 있고, 이 앨범에 저작권이 있는 멜로디가 894개가 있다면, 
평균값은 23.53이 되고 올림해서 24가 된다.


import sys
A, B = map(int, sys.stdin.readline().split())
print(A*(B-1)+1)

'''


'''
브론즈5 3003 킹,퀸,룩,비숍,나이트,폰

체스는 총 16개의 피스를 사용하며, 
킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성되어 있다.


동혁이가 발견한 흰색 피스의 개수가 주어졌을 때, 
몇 개를 더하거나 빼야 올바른 세트가 되는지 구하는 프로그램을 작성하시오.

0 1 2 2 2 7  ->   1 0 0 0 0 1

import sys
chess = [1, 1, 2, 2, 2, 8]
inData = list(map(int, sys.stdin.readline().split()))

for i, data in enumerate(chess):
    print(data - inData[i], end = ' ')

'''





