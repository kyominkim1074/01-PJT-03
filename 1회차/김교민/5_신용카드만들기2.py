import sys

sys.stdin = open("_신용카드만들기2.txt")

#신용카드를 만들기 위한 조건
# 1. 카드 번호는 3, 4, 5, 6, 9로 시작해야 한다.
# 2. 카드 번호에 '-'이 들어갈 수 있으며 '-'를 제외한 숫자는 16개이다.
t = int(input())
able_num = '34569'
for case in range(1, t+1):
    card = ''.join(input().split('-'))
    # '-'를 기준으로 문자열을 나누고 하나의 문자열로 합친다.
    
    if card[0] not in able_num or len(card) != 16:
        result = 0
    else:
        result = 1

    print(f'#{case} {result}')