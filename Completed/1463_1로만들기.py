# 백준  1463  1로 만들기     실버3
# 다이나믹 프로그래밍
'''
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1.  X가 3으로 나누어 떨어지면, 3으로 나눈다.
2.  X가 2로 나누어 떨어지면, 2로 나눈다.
3.  1을 뺀다.
'''

#   짝수(20)면   3을 6번  18,  1을 1번  19    7회
#   홀수(21)면   1을 한 번 빼서 짝수로 만들고, 3을 6번, 2를 1번

import sys
cnt = int(sys.stdin.readline())
rnd = 0 
dp = [0] * (cnt+1)  # 최소 연산 수를 저장하는 dp 테이블

if cnt == 1: print(0); sys.exit(0)
elif cnt < 4: print(1); sys.exit(0)
dp[2] = dp[3] = 1

# cnt의 최소 연산을 구하는 과정에서 이전에 계산된 값을 활용하게 된다.
# 그래서 dp(Dinamic Programming) 구조가 되며 이전 값을 저장할 필요가 있다.
def Divide(Num):
    if Num < 4:   # 이미 최소 연산이 완료된 값이라면 활용
        return dp[Num]
    
    dp[Num] = min(Divide(Num//3) + Num%3, Divide(Num//2) + Num%2) + 1
    return dp[Num]

Divide(cnt)
#print(dp)
print(dp[cnt])

'''
4//2 = 2, 나머지 0    계산 1   정답 2
4//3 = 1, 나머지 1    계산 1   정답 2
5//3 = 1 나머지 2     계산 2   정답 3
5//2 = 2 나머지 1     계산 2   정답 3
6//3 = 2 나머지 0     계산 1   정답 2
6//2 = 3 나머지 0     계산 1   정답 2
7//3 = 2 나머지 1     계산 2   정답 3
7//2 = 3 나머지 1     계산 2   정답 3
8//3 = 2 나머지 2     계산 3  <-out
8//2 = 4 나머지 0     계산 2   정답 3
9//3 = 3 나머지 0     계산 1   정답 2
9//2 = 4 나머지 1     계산 3  <-out

-> 보면 계산 과정은 정답보다 1씩 작다.  그래서 1 더해줌

'''

'''
빠른 계산 결과

testNum = int(input())

dp = {}
dp[1] = 0

def Devidedp(testNum):
    if testNum in dp:
        return dp[testNum]
        
    if(testNum%3 == 0 and testNum%2 == 0):
        dp[testNum] = min(Devidedp(testNum//2),Devidedp(testNum//3))+1
        
    elif(testNum%3 == 0):
        dp[testNum] = min(Devidedp(testNum-1),Devidedp(testNum//3))+1
        
    elif(testNum%2 == 0):
        dp[testNum] = min(Devidedp(testNum-1),Devidedp(testNum//2))+1
        
    else:
        dp[testNum] = Devidedp(testNum-1)+1
    return dp[testNum]



print(Devidedp(testNum))
'''


'''
빠른 결과2

x = int(input())

dp = {}
dp[1] = 0

def rec(x):
    if x in dp:
        return dp[x]
    if(x%3 == 0 and x%2 == 0):
        dp[x] = min(rec(x//2),rec(x//3))+1
    elif(x%3 == 0):
        dp[x] = min(rec(x-1),rec(x//3))+1
    elif(x%2 == 0):
        dp[x] = min(rec(x-1),rec(x//2))+1
    else:
        dp[x] = rec(x-1)+1
    return dp[x]
print(rec(x))

'''