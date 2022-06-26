# 백준 1107 리모컨
# 브루트포스, 백트래킹

'''
수빈이는 TV를 보고 있다. 수빈이는 채널을 돌리려고 했지만, 
버튼을 너무 세게 누르는 바람에, 일부 숫자 버튼이 고장났다.

리모컨에는 버튼이 0부터 9까지 숫자, +와 -가 있다. 
+를 누르면 현재 보고있는 채널에서 +1된 채널로 이동하고, 
-를 누르면 -1된 채널로 이동한다. 

채널 0에서 -를 누른 경우에는 채널이 변하지 않고, 채널은 무한대 만큼 있다.

수빈이가 지금 이동하려고 하는 채널은 N이다. 
어떤 버튼이 고장났는지 주어졌을 때, 
채널 N으로 이동하기 위해서 버튼을 최소 몇 번 눌러야하는지 구하는 프로그램을 작성하시오. 


수빈이가 지금 보고 있는 채널은 100번이다.

5457
3
6 7 8   --> 6

500000
8
0 2 3 4 6 7 8 9   -> 11117

'''
import time # 처리 시간 계산용
start = time.time()

import sys # 입력 처리용
main_ch = 100  # 현재 채널
ch = input() # 이동할 채널
cnt = int(input()) # 고장난 버튼 개수

Move_ch = abs(100 - int(''.join(map(str, ch)))) # 채널 이동 횟수

def IsCh100(ch): # 채널이 100인지 확인
    if ch == '100':  # 100채널 찾는 조건 분기점
        print(0)
        sys.exit(0) # 종료

'''고장난 버튼이 없어서 입력이 0일 때'''
if cnt == 0:
    #-> 그냥 채널 입력, 100채널과 근접하면 +-이동
    IsCh100(ch)
    if Move_ch < len(ch):
        print(Move_ch)
        sys.exit(0)
    else:
        print(len(ch))
        sys.exit(0)    


# 고장난 버튼 집합
nButton = set(sys.stdin.readline().split())

''' 고장난 버튼에 따른 조건 분기'''
if cnt == 10: # 모든 버튼이 고장
    # -> +-로만 채널 이동
    IsCh100(ch)
    print(Move_ch)
    sys.exit(0)

'''입력한 채널이 100이면 즉시 종결'''
IsCh100(ch)

'''여기부터 일반적인 처리 과정 기록'''
Low_num = -1  # 가능한 작은 채널
High_num = 500001 # 가능한 최대 채널
Ch_num = int(''.join(map(str,ch))) # 이동할 채널 정수화

#print(f"{set(ch)=}, {nButton=}")

# 입력 채널 번호에 고장난 버튼이 없을 때
if len(set(ch) & nButton)== 0: 
    print(min(Move_ch, len(ch)))
    sys.exit(0)

'''이동할 채널보다 작은 번호에서 입력 횟수 구하기'''
ableN = Ch_num-1
while ableN > -1 :
    if len(set(str(ableN)) & nButton) > 0:
        ableN -= 1
    else:
        Low_num = len(str(ableN)) + (Ch_num - ableN)
        break

'''이동할 채널보다 큰 번호에서 입력 횟수 구하기'''
ableN = Ch_num+1
while ableN < 1000000:
    if len(set(str(ableN)) & nButton) > 0:
        ableN += 1
    else:
        High_num = len(str(ableN)) + (ableN - Ch_num)
        break    

#print(f"{Low_num=}, {High_num=}")
'''작은 번호에서 경우를 찾지 못했다면(-1) 비교 대상에서 제외함'''
if Low_num == -1:
    print(min(Move_ch, High_num))
else:
    print(min(Move_ch, High_num, Low_num))



print(time.time() - start)


# 반례 참고 https://www.acmicpc.net/board/view/78715

'''
숫자 리스트를 하나의 수로 표현하는 3가지

from functools import *
reduce(lambda x, y : 10 * x + y, a, 0)
12345

>>> ''.join(map(str, a))
12345

>>> ''.join(str(x) for x in a)
12345
'''

