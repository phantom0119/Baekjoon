# 소수 처리 알고리즘

# 소수를 일일이 찾는 과정은 O(X),  X = 개수
# 제곱근(math.sqrt())을 이용하면 효율적으로 줄일 수 있다.


import math
import heapq

def Prime_Number(dlist : list):
    ret = []
    for num in dlist:
        flag = 0
        for n in range(2, int(math.sqrt(num))+1):
            if num % n == 0:
                flag = 1
                break
        
        if flag == 0:
            heapq.heappush(ret, num)
    
    return ret


print(*Prime_Number([i for i in range(2, 50)]))
                


