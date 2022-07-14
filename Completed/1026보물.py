# 백준 1026 보물
# 그리디 알고리즘, 정렬
'''
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.

S = A[0] × B[0] + ... + A[N-1] × B[N-1]

S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.


첫째 줄에 N이 주어진다.
둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고,
셋째 줄에는 B에 있는 수가 순서대로 주어진다.
N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

5
1 1 1 6 0
2 7 8 3 1    -> 18

3
1 1 3
10 30 20         -> 80

9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1           -> 528
'''
import sys
inputF = sys.stdin.readline
T = int(inputF())
A = list(map(int, inputF().split()))
B = list(map(int, inputF().split()))
A = sorted(A, reverse=True)
B = sorted(B)
total = 0
for i in zip(A, B):
    total += i[0]*i[1]
print(total)


