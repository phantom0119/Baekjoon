# 백준 11720 숫자의 합 구하기    브론즈4
# 문자열, 수학

cnt = int(input())  # 숫자의 개수
numlist = input() #문자열 구성의 수 리스트
total = 0 # 최종합

rnd = cnt // 2

# 문자열 길이의 반절만 탐색해서 처리한다 --> 시간 단축
# 주어진 모든 데이터를 전부 더할 것이기 때문에 첫 인덱스, 마지막 인덱스 같이 탐색한다.
# 이 때, i = range(0, cnt//2) 구간
# 그리고 마지막부터 탐색하는 인덱스 값은 -1-i 
for i in range(rnd):
    total += int(numlist[i]) + int(numlist[-1-i])


# 수의 개수가 홀수인 경우, for문으로 중앙값 계산을 하지 않음
# 그래서 최종합에 중앙값 처리하는 방식을 추가.
if cnt % 2 != 0:
    print(total + int(numlist[rnd]))
else:
    print(total)


    