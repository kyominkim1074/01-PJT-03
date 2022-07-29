import sys

sys.stdin = open("_직사각형길이찾기.txt")

t = int(input())
for case in range(1, t+1): #케이스의 개수만큼 반복
    num = list(map(int, input().split()))
    num.sort() #리스트를 정렬시킨다.
    #리스트 안의 큰 수의 개수가 3개일 경우(정사각형)
    #결과값을 큰 수에 대입시킨다.
    if num.count(max(num)) == 3:
        re = max(num)
    #리스트 안의 큰 수의 개수가 1개일 경우(직사각형)
    #결과값을 큰 수에 대입시킨다.
    elif num.count(max(num)) == 1:
        re = max(num)
    #리스트 안의 가장 작은 수의 개수가 1개일 경우
    #결과값에 작은 수를 대입시킨다.
    else:
        re = min(num)
    print(f'#{case} {re}')