'''
z = range

def G(A, i=0):
    if i == len(A):
        return[A[:]]
    r = []
    if A[i] == '.' and (i == 0 or A[i-1] != 'O'):
        A[i] = 'O'
        r += G(A, i+1)
        A[i] = '.'
    r += G(A, i+1)
    return r


def V(u, d):
    for i in z(len(u)):
        if (i != 0 and u[i-1] == 'O' and d[i] == 'O') or (i != len(u)-1 and u[i+1] == 'O' and d[i] == 'O'):
            return False
    return True


for i in z(int(input())):
    n, m = map(int, input().split())
    L = [list(input()) for i in z(n)]
    R = [[] for i in z(n)]

    print(f"L = {L} \n R = {R}\n")
    for i in z(n):
        R[i] = G(L[i])
    C = [[] for i in z(n)]

    print(f"C = {C} \n R = {R}\n")
    for i in z(n):
        for j in R[i]:
            C[i].append(j.count('O'))
    for i in z(n-1):
        for j in z(len(R[i])):
            for k in z(len(R[i+1])):
                if V(R[i][j], R[i+1][k]):
                    C[i+1][k] = max(C[i+1][k], C[i][j]+R[i+1][k].count('O'))
    
    print(f"C = {C} \n")
    print(max(C[-1]))
'''

# 해석 코드
import sys

def Convert_Data() -> list:
    global row
    global col
    convert_data = [[-1]*(col+2) for _ in range(row+2)]

    data = [sys.stdin.readline().strip() for i in range(row)]  # 자리 데이터 입력

    for i in range(row):   # 문자열 데이터를 바탕으로 값 변환
        for j in range(col):
            if data[i][j] == 'x':
                convert_data[i+1][j+1] = -1
            else:
                convert_data[i+1][j+1] = 0
    #print(f"convert_data_set = {convert_data}")
    return convert_data


def Check_Position(list_table :list, type :int):
    global row
    global col
    cnt = 0
    if type == 1:  # 홀수 우선 배치
        pass_token = True
        for c in range(col):   # 홀수 열에 -1을 제외한 공간에 모두 1배치
            if pass_token:
                check_minor_A = 0
                check_minor_B = 0
                for r in range(1,row+1):
                    if list_table[r][c+1] == -1:
                        check_minor_A += 1
                    if list_table[r][c+2] == -1:
                        check_minor_B += 1
                print(f"minor_A = {check_minor_A}, minor_B = {check_minor_B}\n")

                if check_minor_A > check_minor_B:
                    pass_token = False
                
                if (c+1)%2 != 0 and pass_token:
                    for r in range(row):
                        if list_table[r+1][c+1] != -1:
                            list_table[r+1][c+1] = 1
                            cnt += 1
            pass_token = True

        
        for c in range(col):
            if (c+1)%2 == 0:
                for r in range(row):
                    value_list = [list_table[r][c], list_table[r][c+2], list_table[r+1][c], list_table[r+1][c+2],
                                list_table[r+2][c], list_table[r+2][c+2]]
                    print(f"value_list = {value_list} value_list_cnt = {value_list.count(1)}")
                    if value_list.count(1) != 0 or list_table[r+1][c+1] == -1:
                        pass
                    else:
                        list_table[r+1][c+1] = 1
                        cnt += 1
            else:
                pass
    else:
        for c in range(col):   # 짝수 열에 -1을 제외한 공간에 모두 1배치
            if (c+1)%2 == 0:
                for r in range(row):
                    if list_table[r+1][c+1] != -1:
                        list_table[r+1][c+1] = 1
                        cnt += 1
        
        for c in range(col):
            if (c+1)%2 != 0:
                for r in range(row):
                    value_list = [list_table[r][c], list_table[r][c+2], list_table[r+1][c], list_table[r+1][c+2],
                                list_table[r+2][c], list_table[r+2][c+2]]
                    print(f"value_list = {value_list}, value_list_cnt = {value_list.count(1)}")
                    if value_list.count(1) != 0 or list_table[r+1][c+1] == -1:
                        pass
                    else:
                        list_table[r+1][c+1] = 1
                        cnt += 1
            else:
                pass        


    print(f"list_table_odd = {list_table}\n cnt = {cnt}")
    return cnt



for _ in range(int(input())):  # 테스트 케이스 입력
    row, col = map(int, sys.stdin.readline().split())  # 행(row)과 열(col) 개수
    data_table = Convert_Data()  # 입력으로 받은 값을 -1, 0으로 표현

    # 홀수 위치를 기준으로 값 집어 넣기
    odd_cnt = Check_Position(data_table, 1)
    even_cnt = Check_Position(data_table, 0)

    print(max(odd_cnt, even_cnt))
    

    