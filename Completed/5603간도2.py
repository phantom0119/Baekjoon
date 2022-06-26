# 백준 5603 문제2  브론즈2
'''
0에서 9까지의 숫자로만 구성된 문자열이 주어지면
다음 규칙에 따라 새로운 문자열을 만드는 작업을 고려하십시오.

주어진 문자열을 왼쪽 끝
부터 1문자씩 순서대로 읽어 가고, 
같은 숫자 a가 r개 계속되고 있었을 경우, 개수 r과 숫자
a를 공백으로 구분하지 않고이 순서로 내보냅니다.

주어진 문자열의 오른쪽 끝까지 읽고 마지막
내보내기가 끝난 곳까지를 도중 몇 번 내보내기가 있었다고 해도 전부 정리
조작 한 번으로 계산합니다. 2번째 이후의 조작은 전회의 조작에 의해 써낸 문장
문자열을 주어진 문자열로 동일한 작업을 수행합니다.

예를 들어 "122244"라는 문장
문자열이 주어지면 왼쪽 가장자리부터 순서대로 1 개의 1, 3 개의 2, 2 개의 4이므로
조작 1회로 얻어지는 문자열은 “113224”이며, “44444444444”(11개의 4)의 장소
결과는 문자열이 "114"입니다.

100자 이하의 주어진 문자열에 위의 조작을 n 번 실시한 문자열을 출력하는 프로그램을 작성하라. 
그러나 n ≤ 20이라고 가정합니다.

2 행으로 이루어져 1 행째에 조작 회수 n, 2 행째에 최초의 캐릭터 라인이 쓰여져 있다.
1 행으로, 지정된 회수의 조작을 실시한 캐릭터 라인의 뒤에 개행을 넣는다.
'''
# 11 -> 21
# 21 -> 1211
# 1211 -> 111221
# 111221 -> 312211
# 312211 -> 13112221

#그래서 입력이 5 \n 11 이면 -> 13112221
case = int(input())
start = input()

for _ in range(case):
    rnd = ''
    cnt = 1
    for i in range(len(start)-1):
        if start[i] == start[i+1]:
            #print(f"in {start[i]=} {start[i+1]=}")
            cnt += 1
            if i+1 == len(start)-1:
                rnd += str(cnt) + start[i]
        else:
            #print(f"else {start[i]=} {start[i+1]=}")
            rnd += str(cnt) + start[i]
            cnt = 1
            if i+1 == len(start)-1:
                rnd += '1' + start[i+1]
            
    start = rnd
print(start)


'''
기인

n=int(input())
d=input()
for _ in range(n):
    t=''
    p=d[0]
    l=0
    for i in d:
        if i==p:l+=1
        else:
            t+=str(l)+p
            p,l=i,1
    t+=str(l)+p
    d=t
print(d)


n,l=int(input()),input()
from itertools import*
for i in range(n):l=''.join(str(len([*w]))+v for v,w in groupby(l))
print(l)
'''


