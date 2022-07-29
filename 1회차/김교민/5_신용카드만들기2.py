import sys

sys.stdin = open("_신용카드만들기2.txt")

t = int(input())
for case in range(1, t+1):
    card_num = list(map(int, input().split()))
    
def luhn(number):
    digit_ = len(number)
    sum_ = 0
    is_ = False
    
    for i in range(digit_ -1, -1, -1):
        d = ord(number[i]) - ord('0')
        
        if (is_ == True):
            d = d*2
        
        sum_ += d//10
        sum_ += d%10
        is_ = not is_
    if (sum%10 == 0):
        return True
    else:
        return False
    
head_num = ['3', '4', '5', '6', '9']
    
for i in range(len(card_num)):
        if card_num[i] == (i%2 == 0):
            list_.append(i*2)
        elif card_num[i] == (i%2!=0):
            list_.append(i)
        result = sum(list_)
        if result%10 != 0:
            d