value_list = []

while(True):
    input_value = int(input())
    
    if (input_value == -1): break
    else:
        value_list.append(input_value)

cnt = len(value_list)

for i in range(cnt):
    N = value_list[i]
    cntN = 0
    print(f"N={N}:")
    if(N%1111 == 0 or N > 9999 or N < 1000):
        print("No!!")
    else:
        while(True):
            num1 = "".join(sorted(str(N))).lstrip("0")
            num2 = "".join(sorted(str(N), reverse=True))

            N = int(num2) - int(num1)

            print(f"{num2}-{num1}={N}")
            cntN += 1
            if (N==0 or N==6174):
                print(f"Ok!! {cntN} times")
                break