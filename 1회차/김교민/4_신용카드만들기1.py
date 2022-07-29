import sys

sys.stdin = open("_신용카드만들기1.txt")
t = int(input())
for case in range(1, t+1):
    card_num = list(map(int, input().split()))
    list_ = []
    for i in range(len(card_num)):
        if i == (i%2 == 0) or i == 0:
            list_.append(card_num[i]*2)
        elif i == (i%2==1):
            list_.append(card_num[i])
    result = sum(list_)
    nn = result%10
    print(nn)