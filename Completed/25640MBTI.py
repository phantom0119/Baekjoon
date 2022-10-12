# 백준 25640 MBTI  브론즈4
# 문자열, 구현

ret = input()
N = int(input())
num = 0
for _ in range(N):
    if input() == ret:
        num += 1

print(num)