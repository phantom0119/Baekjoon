# 백준 2525 오븐시계  브론즈3
'''
훈제오리구이를 시작하는 시각과 
오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 

오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

14 30
20      -> 14 50 
'''
#import sys
# Hour, Minute = map(int, sys.stdin.readline().split())
# Plus = int(sys.stdin.readline().split())
Hour, Minute = map(int, input().split())
Plus = int(input())

Minute = Minute + Plus
Hour = Hour + Minute//60
Minute = Minute%60

if Hour >= 24:
    Hour = Hour%24

print(Hour, Minute)