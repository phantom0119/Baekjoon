# 백준 별찍기-10  실버1
# 재귀, 분할정복
import sys
sys.setrecursionlimit(10 ** 6)  # 파이썬 재귀함수 제한 해제
                                # 파이썬은 기본 제한이 1000이기 때문

def MakeStars(cnt):
    if cnt == 3:   # 가장 말단까지 왔을 경우
        output = ['***', '* *', '***']
        return output
    else:
        Pattern = MakeStars(cnt//3)   # cnt = 9면   3
        output = []
        for Line1 in Pattern:  # cnt = 9면, ['***', '* *', '***'] 가져옴
            output.append(Line1*3)
        for Line2 in Pattern:
            output.append(Line2 + ' '*(cnt//3) + Line2)
        for Line3 in Pattern:
            output.append(Line3*3)
        return output

cnt = int(input())
print('\n'.join(MakeStars(cnt)))