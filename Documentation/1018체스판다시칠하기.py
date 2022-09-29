# 백준 1018 체스판 다시 칠하기


'''
ROW, COL = map(int, input().split())
Insert_List = []
Low = 64

W_First = ['W','B','W','B','W','B','W','B'] 
B_First = ['B','W','B','W','B','W','B','W']

for i in range(ROW):
    Insert_List.append(input())

# --------------------------------
#    전수조사로 최솟값 찾아보기
# --------------------------------
for i in range(ROW-7):
    for j in range(COL-7):
        cnt_W = 0 # W시작인 배열 카운트
        cnt_B = 0 # B시작인 배열 카운트
        Comp_List = [col[j:j+8] for col in Insert_List[i:i+8]]
        #print(f" Value = {Comp_List}")


        for k in range(8):
            if k%2 == 0:
                for m in range(8):
                    if Comp_List[k][m] != W_First[m]:
                        cnt_W += 1
                    elif Comp_List[k][m] != B_First[m]:
                        cnt_B += 1
            elif k%2 == 1:
                for m in range(8):
                    if Comp_List[k][m] != B_First[m]:
                        cnt_W += 1
                    elif Comp_List[k][m] != W_First[m]:
                        cnt_B += 1

        #print(cnt_W, cnt_B)
        Low = min(Low, cnt_W, cnt_B)

print(Low)

'''
# https://dojang.io/mod/page/view.php?id=2460
import sys
inputF = sys.stdin.readline
N, M = map(int, inputF().split())

# White 시작인 경우와 Black 시작인 경우
White = int('0b10101010',2)
Black = int('0b01010101',2)

# 사용자 입력 판
board = [] 

# 판에 값 입력 받기 (W=1, B=0)
for _ in range(N):
    text = inputF().rstrip()
    text = text.replace('W', '1')
    text = text.replace('B', '0')
    board.append(list(map(str, text)))


ret = 64 # 최대로 바꿀 수 있는 값
for i in range(M-7): # 열 시작 인덱스
    for j in range(N-7): # 행 탐색
        base = 0
        for k in range(j, j+8):
            # 행의 값을 2진수 문자열로 사용
            a = '0b' + ''.join(board[k][i:i+8])

            if k % 2 == 0:
                base += bin(int(a,2) ^ White).count('1') # XOR 결과 카운트
            else:
                base += bin(int(a,2) ^ Black).count('1')
            
        ret = min(ret, base, 64-base)
        
print(ret)

'''
n, m = map(int, input().split())
li = [list(input().strip()) for i in range(n)]
ans = n * m
WB = ["W", "B"]


# W와 B를 각각 1과 0으로 변환하는 과정
for i in range(n):
    for j in range(m):
        li[i][j] = (li[i][j] == WB[(i + j) % 2])


# a가 특정 하나의 계산 결과면 64-a는 반대되는 결과?
# 실제로 W가 우선할 때 45면 B의 경우는 19가 된다 (45+19=64)
for i in range(n - 7):
    for j in range(m - 7):
        a = sum([sum(li[k][j:j + 8]) for k in range(i, i + 8)])
        a = min(a, 64 - a)
        ans = min(ans, a)
print(ans)
'''