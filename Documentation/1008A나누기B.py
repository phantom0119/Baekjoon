# 백준 1008 A/B
import sys
A, B = map(int, sys.stdin.readline().split())
print(A/B)

'''
과거의 나 (while과 예외처리 사용한 경우)

while True:
    try:
        a, b = input().split()
        num1 = float(a)
        num2 = float(b)
        if num1 <1 or num2 >9:
            continue
        break
    except ValueError:
        print("두 수를 모두 입력하거나 정수 값을 입력하세요.")
print(num1/num2)

'''