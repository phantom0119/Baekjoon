# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
'''
 입출력에 대한 정리
 일반적인 1줄 입력은 input을 사용해도 무관하지만,
 다중 입력 시에는 시관초과로 인해 오답이 될 수 있다.

 ->  sys.stdin.readline() 함수를 사용해서 입력을 진행한다.
 사용법은 input()이랑 동일함.

 split, map, 전부 호환 가능
'''

# 백준 18108 "1998년생인 내가 태국에서는 2541년생?!""
Year = int(input())
print(Year - 543)
