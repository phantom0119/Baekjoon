# 백준 15439 Vera and Outfits
# 조합론인가?
'''
Vera는 N 상의와 N 바지를 소유하고 있습니다. 
i번째 상의와 i번째 바지는 1 ≤ i ≤ N에 대해 색상 i를 가지며, 
    여기서 모든 N 색상은 서로 다릅니다.

의상은 상의 1개와 바지 1개로 구성되어 있습니다. 
베라는 상의와 바지가 같은 색이 아닌 옷을 좋아한다.
그녀는 얼마나 많은 다른 의상을 좋아합니까?

Vera가 좋아하는 다른 의상의 수로 한 줄을 출력합니다.
'''
N = int(input())
cnt = 0 
for i in range(N-1):
    cnt += (N-i)-1

print(cnt*2)


# # A B C D E, A B C D E
# -> A = B C D E
#    B = C D E
#    C = D E
#    D = E
# 더블 20

# A B, A B
# A = B
# 더블 2