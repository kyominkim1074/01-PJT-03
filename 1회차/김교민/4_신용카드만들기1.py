import sys

sys.stdin = open("_신용카드만들기1.txt")
t = int(input())
for case in range(1, t+1):
    card_num = list(map(int, input().split()))
    plus = 0
    for i in range(len(card_num)):
        if (i+1)%2 == 0: #홀수 자리 수
            plus += card_num[i]
        else: #짝수 자리수
            plus += card_num[i]*2
    # 마지막 16번째 숫자를 구하기 위해 반복문을 작성
    for j in range(10):
        tmp = plus + j
        if tmp%10 == 0:
            result = j
            break
    
    print(f'#{case} {result}')