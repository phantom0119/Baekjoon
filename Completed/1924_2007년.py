# 백준 1924 2007년 브론즈1
'''
오늘은 2007년 1월 1일 월요일이다. 
그렇다면 2007년 x월 y일은 무슨 요일일까? 
이를 알아내는 프로그램을 작성하시오.
'''

MonthDict =  {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
DayDict = {1:'MON', 2:'TUE', 3:'WED', 4:'THU', 5:'FRI', 6:'SAT', 0:'SUN'}

def CheckDay(Month, Day):
    cnt = 0
    if Month == 1:
        print(DayDict[Day%7])
    else:
        nDay = 0
        for i in range(1, Month):
            nDay = nDay + MonthDict[i]
            #print(nDay)
        print(DayDict[(Day+nDay)%7])
        
x, y = map(int, input().split())
CheckDay(x, y)


