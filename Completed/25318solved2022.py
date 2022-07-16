# 백준 25318   solved.ac 2022   실버1
# 구현

'''
834일 6시간 = 834.25.
년 계산 =>   834.25 / 365  ~ 2.286

가장 마지막 의견 = 가장 최근 의견 = 0
'''

'''
import datetime
day_1 = datetime.date(year=2020, month=8, day=1)
day_2 = datetime.date(year=2021, month=10, day=14)
time_1 = datetime.timedelta(hours= 10 , minutes=20, seconds=30)
time_2 = datetime.timedelta(hours= 20, minutes=30, seconds=45)
print(time_2 - time_1)
days = list(str(day_2 - day_1).split())
print(days[0])
'''

import datetime
import sys
inputF = sys.stdin.readline

cnt = int(inputF())

if cnt == 0:
    print(0)
    sys.exit(0)

opinion = []
for i in range(cnt):
    opinion.append(inputF().split())

opinion.sort(key= lambda x: x[0])
# 여기까지 값 입력받는 과정
#print(opinion)

days = opinion[-1][0] + opinion[-1][1]  # 가장 최근의 날짜 정보
#days += ''.join(opinion[-1][1].split(':'))
days_date = datetime.datetime.strptime(days, "%Y/%m/%d%H:%M:%S")
#print(days)


p1list = list()
p2list = list()
for idx, i in enumerate(opinion): 
    # tmp = ''.join(i[0].split('/'))  # 날짜 비교를 위한 값
    # tmp += ''.join(i[1].split(':'))
    #tmp_date = datetime.datetime.strptime(tmp, "%Y%m%d%H%M%S")

    '''
    i[0] = 날짜
    i[1] = 시간
    i[2] = 점수
    '''
    tmp = i[0] + i[1]  # 비교할 날짜 정보
    tmp_date = datetime.datetime.strptime(tmp, "%Y/%m/%d%H:%M:%S")

    result = str(days_date - tmp_date).split()
    #print(result)

    if len(result) == 1: # 같은 날짜고 시간만 다르면 리스트 길이 1임
        Y = result[0].split(':')
        Y = int(Y[0])/24
        Y = round(Y/365, 3)

        Y1 = 0.5**Y
        Y2 = 0.9**(cnt-(idx+1))
        Ydata = round(max(Y1, Y2),3)

        #print(f"Y1= {0.5**Y},  Y2={0.9**(cnt-(idx+1))}")
    else:
        Y = list(result[2].split(':'))
        Y = int(Y[0])/24
        Y += int(result[0])
        Y = round(Y/365, 3)

        Y1 = 0.5**Y
        Y2 = 0.9**(cnt-(idx+1))
        Ydata = round(max(Y1, Y2),3)

        #print(f"Y1= {0.5**Y},  Y2={0.9**(cnt-(idx+1))}")


    p1list.append(Ydata * int(i[2]))
    p2list.append(Ydata)

    #print(f"{Y=} {Ydata=}  {int(i[2])=}  {Ydata * int(i[2])}")

print(round(sum(p1list)/sum(p2list),2))
#print(p1list)
#print(p2list)