# 백준 1018 체스판 다시 칠하기

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