# 백준 1051 숫자 정사각형 실버3
# 브루트포스
'''
N×M크기의 직사각형이 있다. 
각 칸에는 한 자리 숫자가 적혀 있다. 
꼭짓점에 쓰여 있는 수가 모두 같은 가장 큰 정사각형을 찾는 프로그램을 작성하시오. 
이때, 정사각형은 행 또는 열에 평행해야 한다.

'''
import sys
inputF = sys.stdin.readline
N, M = map(int, inputF().split())
MaxSize = min(N,M) # 만들 수 있는 가장 큰 정사각형
square = []
Size_list = [1]*10

for _ in range(N):
    square.append(list(inputF().strip('\n')))


for row in range(N):
    for col in range(M-1):
        for cnt in range(MaxSize):
            try: 
                #print(f"{row=} {col=} {cnt=}")
                if square[row][col] == square[row][col+cnt] ==\
                    square[row+cnt][col] == square[row+cnt][col+cnt]:
                    var = int(square[row][col])
                    Size_list[var] = max((cnt+1)**2, Size_list[var])
            except IndexError:
                break

print(max(Size_list))

'''
다른 인원 정답

N, M = map(int, input().split())
matrix = [list(input()) for _ in range(N)]
flag = False
for size in range(min(N, M), 0, -1):
    if flag: break
    for n in range(N - size + 1):
        if flag: break
        for m in range(M - size + 1):
            if matrix[n][m] == matrix[n + size - 1][m] == matrix[n][m + size - 1] == matrix[n + size - 1][m + size - 1]:
                print(size ** 2)
                flag = True
                break


'''