#  백준 9012 괄호 실버4
'''
두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.

괄호의 모양이 바르게 구성된 문자열을 
올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 

한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다. 
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 
그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다. 
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 
그리고 “(()” 는 모두 VPS 가 아닌 문자열이다.


'''
import sys
inputF = sys.stdin.readline
cnt = int(inputF())
strList = []
for _ in range(cnt):
    strList.append(inputF())

for Bracket in strList:
    strStack = ""
    for s in Bracket:
        if strStack == "":
            strStack += s
            continue
        
        if strStack[-1] == '(' and s == ')':
           strStack = strStack[:-1]
        else:
            strStack += s
        
        #print(f"rnd stack = {strStack}")
    
    #print(f"return = {len(strStack)}")
    if strStack[:-1] == "":
        print("YES")
    else:
        print("NO")

'''
import sys
input = sys.stdin.readline

def is_VPS(string):
    count = 0
    for s in string:
        if s == "(":
            count += 1
        else:
            count -= 1
        if count < 0:
            return False
    if count == 0:
        return True
    else:
        return False

T = int(input())
for _ in range(T):
    s = input().strip()
    if is_VPS(s):
        print("YES")
    else:
        print("NO")
'''