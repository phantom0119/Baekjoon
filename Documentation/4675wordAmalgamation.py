# 백준 4675 Word Amalgamaion (단어 융합)  브론즈1
# 


'''
1) 1~100 개의 단어를 가지는 사전.  (XXXXXX 문자열을 만날때까지 입력 받는다.)
2) 1개 이상의 스크램블 단어. (XXXXXX 문자열을 만날때까지 입력 받는다.)
사전의 단어는 정렬될 필요는 없지만 고유해야 한다.
모든 words들은 소문자이고, 최소 1개에서 6개의 문자열 길이를 가진다.
'''
import sys
inputF = sys.stdin.readline
OUT = 'X'*6
words_dict = {}

def input_words():
    while True:
        text = inputF().rstrip()
        if text == OUT:
            break
        else:
            tmp = ''.join(sorted(text))
            if tmp in words_dict:  # scramble words가 사전에 있다면
                words_dict[tmp] += [text]
            else:   # 사전에 없다면 항목 생성
                words_dict[tmp] = [text]

def scram_words():
    while True:
        text = inputF().rstrip()
        if text == OUT:
            break
        else:
            text = ''.join(sorted(text))
            if text in words_dict:
                for t in words_dict[text]:
                    print(t)
            else:
                print('NOT A VALID WORD')
        print('******')

if __name__ == '__main__':
    input_words()
    

    # 사전에 등록된 단어를 오름차순 정렬해 둔다.
    for i in words_dict:
        words_dict[i] = sorted(words_dict[i])

    scram_words()
    print(words_dict)

'''
# 야미 코드

d, X={}, 'X'*6

# 사전 입력에 대한 부분
while 1:
    s=input() 
    k=''.join(sorted(s))

    if s == X: 
        break

    if k in d: 
        d[k] += [s]
    else:
        d[k] = [s]

for i in d:
    d[i] = sorted(d[i])

# Scramble 처리에 대한 부분
while 1:
    s=''.join(sorted(input()))

    if s==X:
        break

    if s in d:
        for i in d[s]:
            print(i)
    else:
        print('NOT A VALID WORD')
    print('*'*6)

'''