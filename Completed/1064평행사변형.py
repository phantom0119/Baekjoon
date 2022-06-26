from math import sqrt

point_value = list(map(int, input().split()))
x_list = list()
y_list = list()

for i in range(6):
    if i%2 == 0:
        x_list.append(point_value[i])
    else:
        y_list.append(point_value[i])

# 기울기가 같은지 검사하는 함수
def Check_Gradient(x_list :list, y_list :list) -> bool:
    gradient_A = (x_list[2] - x_list[0]) * (y_list[1] - y_list[0])
    gradient_B = (x_list[1] - x_list[0]) * (y_list[2] - y_list[0])

    if gradient_A == gradient_B:
        return True
    else:
        return False

# 두 점 사이의 길이 계산 함수
def Side_Length(list1 :list, list2 :list) -> float:
    return sqrt((list2[0]-list1[0])**2 + (list2[1]-list1[1])**2)


# 1. 기울기가 같은지 검사하기
if Check_Gradient(x_list, y_list) == True:
    print(-1.0)
else:
    point_A = [x_list[0], y_list[0]]
    point_B = [x_list[1], y_list[1]]
    point_C = [x_list[2], y_list[2]]
    
    length_AB = Side_Length(point_A, point_B)
    length_AC = Side_Length(point_A, point_C)
    length_BC = Side_Length(point_B, point_C)

    max_value = max(length_AB, length_AC, length_BC)
    min_value = min(length_AB, length_AC, length_BC)

    print((max_value - min_value)*2)
