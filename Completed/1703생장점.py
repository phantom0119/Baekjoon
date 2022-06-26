# 백준 1703 생장점 브론즈3
'''
각 줄은 나무의 나이 a(1 ≤ a ≤ 20)로 시작하며, 
그 뒤로 2a 개의 정수가 공백을 두고 주어집니다. 
2a 개의 정수는 splitting factor와 
가지치기 한 가지의 수가 level 별로 나열된 것입니다.

마지막 줄로  '0'이 주어지며 더 이상의 입력은 없습니다. '0'은 처리하지 않습니다.
'''
import sys
inputF = sys.stdin.readline
while True:
    branchorama = list(map(int, inputF().split()))
    level = branchorama[0]
    
    if level == 0:
        sys.exit(0)

    leaf = 1
    factor = branchorama[1::2]
    pruning = branchorama[2::2]
    #print(f"{level=}, {factor=}, {pruning=}")
    
    for rnd in zip(factor, pruning):
        leaf = (leaf * rnd[0]) - rnd[1]
    
    print(leaf)


'''
while True:
    
    lst = list(map(int,input().split()))

    if lst[0] == 0:
        break
    else:
        result = 0
        rangenum = lst[0] * 2
        
        for i in range(1,rangenum):
            if i == 1:
                result = lst[i] - lst[i+1]
            elif i % 2 == 1:
                result = result - lst[i+1]
            else:
                result = result * lst[i+1]

        print(result)
'''