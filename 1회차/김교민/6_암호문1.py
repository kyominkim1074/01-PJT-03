import sys

sys.stdin = open("_암호문1.txt")

for t in range(1, 11):
    N = int(input()) #원본 암호문의 길이
    P = list(map(int, input().split())) # 원본 암호문
    Command_N = int(input()) #명령어 개수
    Com_ = list(input().split())
    
    chan = ''
    a = -1
    b = -1
    for i in range(len(Com_)):
        if Com_[i] == 'I':
            chan = Com_[i]
            a = -1
            b = -1
        else:
            if chan == 'I':
                d