# 브론즈2 1408 24

'''
도현이는 선영이를 임무를 시작한지 정확하게 24시간이 되는 순간에 잡으려고 한다.

만약 지금 시간이 13:52:30이고, 
임무를 시작한 시간이 14:00:00 이라면 도현이에게 남은시간은 00:07:30 이다.

모든 시간은 00:00:00 ~ 23:59:59로 표현할 수 있다. 

입력과 출력에 주어지는 모든 시간은 XX:XX:XX 형태이며, 
숫자가 2자리가 아닐 경우에는 0으로 채운다.

'''


now = input()   # 현재시간
start = input() # 임무시간

hour, minute, second = map(int, now.split(':'))       # 현재시간 3분할
Shour, Sminute, Ssecond = map(int, start.split(':'))  # 임무시간 3분할
#print(f"{hour=}, {minute=}, {second=}")

if second > Ssecond :  # 현재(초) > 임무(초)
    second = 60 - second + Ssecond
    minute += 1
else:
    second = Ssecond - second

if minute > Sminute :  # 현재(분) > 임무(분)
    minute = 60 - minute + Sminute
    hour += 1 
else:
    minute = Sminute - minute

if hour > Shour :      # 현재(시) > 임무(시)
    hour = 24 - hour + Shour
else:
    hour = Shour - hour

print("%02d:%02d:%02d" % (hour, minute, second))



