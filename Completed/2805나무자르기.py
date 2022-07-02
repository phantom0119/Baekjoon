# 백준 2805 나무 자르기   실버2
# 이분탐색, 매개변수 탐색
'''
목재절단기는 다음과 같이 동작한다. 
먼저, 상근이는 절단기에 높이 H를 지정해야 한다. 
높이를 지정하면 톱날이 땅으로부터 H미터 위로 올라간다. 
그 다음, 한 줄에 연속해있는 나무를 모두 절단해버린다. 
따라서, 높이가 H보다 큰 나무는 H 위의 부분이 잘릴 것이고, 
낮은 나무는 잘리지 않을 것이다. 예를 들어, 
한 줄에 연속해있는 나무의 높이가 20, 15, 10, 17이라고 하자. 
상근이가 높이를 15로 지정했다면, 
나무를 자른 뒤의 높이는 15, 15, 10, 15가 될 것이고, 
상근이는 길이가 5인 나무와 2인 나무를 들고 집에 갈 것이다. 
(총 7미터를 집에 들고 간다) 절단기에 설정할 수 있는 높이는 양의 정수 또는 0이다.

상근이는 환경에 매우 관심이 많기 때문에, 
나무를 필요한 만큼만 집으로 가져가려고 한다. 
이때, 적어도 M미터의 나무를 집에 가져가기 위해서 
절단기에 설정할 수 있는 높이의 최댓값을 구하는 프로그램을 작성하시오.

'''
import sys
N, M = map(int, sys.stdin.readline().split())
Tree = list(map(int, sys.stdin.readline().split()))
Tree.sort()

MaxH = Tree[-1] # 최댓값
MinH = 0  # 최솟값
MidH = (MaxH+MinH)//2 # 중앙값(계산용)
ret = 0

while True:
    GetH = 0
    for i in Tree: # 나무를 잘라 얻은 길이
        if i >= MidH: GetH += (i-MidH)

    if GetH >= M: # 길이를 충족한다면
        ret = max(ret, MidH)
        MinH = MidH
        MidH = (MaxH+MinH)//2
    elif GetH == M:  # 원하는 길이와 똑같다면
        print(ret)
        break
    else:
        MaxH = MidH
        MidH = (MaxH+MinH)//2        

    if MaxH - MinH == 1:
        print(ret)
        break


'''
python3로 맞은 답안

N,M = map(int,input().split())
Tree = list(map(int,input().split()))
Tree.sort(reverse=True)
if N > 1:
    a = Tree[0]-Tree[1]
    num,i = 1,0
    while a < M and i < N-2:
        i += 1
        num += 1
        a += (Tree[i]-Tree[i+1])*num

    if a == M:
        print(Tree[num])
    elif a < M:
        if (M-a)%N:
            print(Tree[-1]-((M-a)//N+1))
        else:
            print(Tree[-1]-((M-a)//N))   
    else:
        print(Tree[num]+(a-M)//num)
else:
    print(Tree[0]-M)
'''