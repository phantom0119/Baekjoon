#백준 1343 폴리오미노 실버5
'''
폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB
'.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, 
'.'는 폴리오미노로 덮으면 안 된다.
폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.
'''
import sys
str_list = input().split('.')
ret = ''
for str in str_list:
    size = len(str)
    if size > 2 and size%2 == 0:
        ret += 'AAAA' * (size//4)
        size -= 4 * (size//4)
    elif size==2:
        ret += 'BB'
        size -= 2
    elif size == 0:
        pass
    else:
        print('-1')
        sys.exit(0)

    if size == 2:
        ret += 'BB'  
    ret += '.'
    

print(ret[:-1])

'''
헐...

N=input()
N=N.replace("XXXX","AAAA")
N=N.replace("XX","BB")
if 'X' in N:
    print(-1)
    
else:
    print(N)


import sys
input = sys.stdin.readline
# input = int(sys.stdin.readline())


arr =input().replace("XXXX","AAAA").replace("XX","BB")

if "X" in arr:
    print(-1)
else:
    print(arr)
'''