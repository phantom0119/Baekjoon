# 백준 1032  명령 프롬프트   브론즈1
# 구현, 문자열
search = list()
search_cnt = int(input())
question_text = list()

for i in range(search_cnt):
    search.append(input())

cnt = len(search[0])

for i in range(cnt):   # 텍스트 개수
    q_mark = False
    text = search[0][i]
    for j in range(search_cnt):  # 검색 개수
        if text != search[j][i]:
            q_mark = True
            break
    
    if q_mark:
        question_text.append("?")
    else:
        question_text.append(text)

print(''.join(question_text))