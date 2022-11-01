# 백준 2023  신기한 소수   골드5
# 그래프이론, DFS 깊이우선 탐색

import sys
sys.setrecursionlimit(10**6) # 파이썬 제귀 제한 해제
prime = [2, 3, 5, 7]  # 1의 자리 중 소수인 수
C = [1, 3, 5, 7, 9]   # 함수에서 사용할 소수 찾기 리스트
ret = [] # 최종 출력 리스트

N = int(input())  # 자리 수
check = 1 # rnd 수 (N자리까지 왔는지 확인)

# num=수, rnd = 자리수
# 뒤에 올 수 있는 수는 2의 배수가 아닌 수
# 2의 배수이면 2로 나누어지기 때문
def check_prime(num, rnd):
    for i in C: # [1, 3, 5, 7, 9]
        flag = 0
        tmp = num*10 + i

        # 2는 사전에 제외했기 때문에 3부터 검사
        # 제곱근 수까지 검사해서 시간복잡도 줄임
        for j in range(3, int(tmp**0.5)+1):
            if tmp % j == 0:  # 나눠지는 수가 있으면 차단
                flag = 1
                break
        
        if flag == 0:
            if rnd == N-1: # N자리까지 도달했으면 저장
                ret.append(tmp)
            else:
                check_prime(tmp, rnd+1)

if N != 1:
    for pr in prime:
        check_prime(pr, check)
else: # N==1일 때 즉시 처리
    for i in prime: print(i)

# 최종 출력 (N==1이면 어차피 ret는 값이 없어서 상관이 없다.)
for i in ret:
    print(i)