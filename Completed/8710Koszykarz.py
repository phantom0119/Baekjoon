# 백준 8710 Koszykarz  브론즈4
# 수학, 사칙연산
from math import ceil
k, w, m = map(int, input().split())
diff = ceil((w-k)/m)
print(diff)