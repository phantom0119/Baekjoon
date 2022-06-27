# 백준 1874 스택 수열   실버2
# 자료구조 스택
'''
스택은 자료를 넣는 (push) 
입구와 자료를 뽑는 (pop) 
입구가 같아 제일 나중에 들어간 자료가 제일 먼저 나오는 (LIFO, Last in First out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 
하나의 수열을 만들 수 있다. 
이때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자. 
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지, 
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 
이를 계산하는 프로그램을 작성하라.

'''
import sys
inputF = sys.stdin.readline

if __name__ == '__main__':
    CNT = int(inputF())
    Stk = []
    Ret = []
    Last_Pin = 0
    for _ in range(CNT):
        Pin = int(inputF())

        if Last_Pin < Pin:  # 스택에 값을 추가해야 하는 경우
            for i in range(Last_Pin+1, Pin+1):
                #print(f'i = {i}')
                Stk.append(i)
                Ret.append('+')
            
            Ret.append('-') # 마지막에는 해당 값을 추출
            del(Stk[-1])
            Last_Pin = Pin  # 사용한 값의 최댓값
            #print(f"round1 Stk = {Stk}, LastPin = {Last_Pin}")
        
        elif Last_Pin > Pin: # 사용 가능한 수를 벗어났는지 확인
            if  len(Stk) == 0 or Stk[-1] < Pin:
                print('NO')
                sys.exit(0)
            else:
                while True:
                    if Stk[-1] != Pin:
                        Ret.append('-')
                        del(Stk[-1])
                    elif Stk[-1] == Pin:
                        Ret.append('-')
                        del(Stk[-1])      
                        break                  
            #print(f"round2 Stk = {Stk}, LastPin = {Last_Pin}")
                    

    for txt in Ret:
        print(txt)




'''
n = int(input())
stack = []
result = []
no_answer = True
count = 0

for i in range(n):
    x = int(input())

    while count < x:
        count += 1
        result.append("+")
        stack.append(count)

    if x == stack[-1]:
        stack.pop()
        result.append("-")
    else:
        no_answer = False
        break


if no_answer == False:
    print("NO")
else:
    print("\n".join(result))
'''