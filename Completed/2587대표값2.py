# 백준 2587  대표값2    브론즈2
# 수학, 구현, 사칙연산
import sys
L = []
for _ in range(5):
    L.append(int(sys.stdin.readline()))

L.sort()
print(sum(L)//5)
print(L[2])