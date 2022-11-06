import sys
input = sys.stdin.readline
# N=개수, i 번째에서 j번째 수까지 합
N, M = map(int, input().split())
arr = list(map(int, input().split()))
sumarr = [0 for _ in range(N+1)]

# 각 원소의 누적 합 구하기
tmp = 0
for idx, num in enumerate(arr):
    tmp += num
    sumarr[idx+1] = tmp
    
#print(sumarr)
# 테스트 케이스 계산하기
for _ in range(M):
    i, j = map(int, input().split())
    print(sumarr[j] - sumarr[i-1])

