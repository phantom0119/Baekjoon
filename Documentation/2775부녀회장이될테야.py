# 백준 2775 부녀회장이 될테야   브론즈1
# 다이나믹 프로그래밍 (점화식, 재귀)

'''
다이나믹 프로그래밍은 재귀를 활용해 Bottom-UP 구조로 처리하거나
Memoization 방식으로 전 처리 값을 저장해 활용하는 방식으로 적용한다.

K층의 N호 인원 수 = K층의 (N-1)호 + (K-1)층의 N호
단 0층은 1호~N호의 인원이 1~N명임.
'''
import sys
sys.setrecursionlimit(10**6)
inputF = sys.stdin.readline


def k_floor_n_room(apart, k, n):
    if k == 0:
        return n
    elif n == 1:
        return 1
    else:
        tmp = k_floor_n_room(apart, k, n-1) + k_floor_n_room(apart, k-1, n)
        apart[k][n] = tmp
        return tmp
        

T = int(inputF()) # TCase
for _ in range(T):
    # k:층, n:호실
    k=int(inputF()); n=int(inputF())
    
    # 아파트 층 인원 수 구조
    Apart = [[0] * (n+1) for _ in range(k+1)]
    for i in range(1,n+1):
        Apart[0][i] = i # 0층 처리

    tmp = k_floor_n_room(Apart, k, n)
    print(tmp)
    
    #print(Apart)


'''
위의 코드는 재귀를 이용한 다이나믹 프로그래밍 해답이다.
하지만, 문제에서는 [시간초과]를 발생시킨다.

따라서 적절한 다른 방법이 필요하다.
'''

T = int(input())

for i in range(T):
    floor = int(input())
    room = int(input())
    #0층의 room호실까지의 값을 우선 저장
    apart = [val for val in range(1,room+1)]

    for _ in range(floor):
        for ro in range(1, room):
            apart[ro] += apart[ro-1]

    print(apart[room-1])