# 백준 1003 피보나치 함수
# 재귀함수

'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}

1은 2번 출력되고, 0은 1번 출력된다.
N이 주어졌을 때, fibonacci(N)을 호출했을 때,
0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.
'''
import sys
inputF = sys.stdin.readline
T = int(inputF())
Cnt0 = [1, 0]
Cnt1 = [0, 1]
'''
 3이면  2+1  (1+0) + 1
 4이면  3+2+1  ((1+0)+1) + (1+0) + 1
 입력 수의 전 수와 전전수를 더한다.
 이는 0과 1의 개수도 전 수와 전전 수의 값에 영향을 받는다는 의미.
'''
#Cnt1 = 0
#Cnt0 = 0
def FiboCnt(N : int):
    global Cnt1, Cnt0
    if N == 0:
        Cnt0 += 1
    elif N == 1:
        Cnt1 += 1
    else:
        FiboCnt(N-1)
        FiboCnt(N-2)

def ZeroOneCount(N : int):
    for i in range(2, N+1): # 0과 1은 직접 처리함
        Cnt0.append(Cnt0[i-1]+Cnt0[i-2])
        Cnt1.append(Cnt1[i-1]+Cnt1[i-2])


for _ in range(T):
    N = int(inputF())
    if N == 0:
        print("1 0")
    elif N == 1:
        print("0 1")
    else:
        ZeroOneCount(N)
        print(f"{Cnt0.pop()} {Cnt1.pop()}")
    # 1회분 끝났으면 초기화
    Cnt0 = [1, 0]
    Cnt1 = [0, 1]