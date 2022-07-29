import sys

sys.stdin = open("_소득불균형.txt")

t = int(input()) #테스트 케이스의 수
for case in range(1, t+1): # 케이스의 수만큼의 범위 내에서 각각 값을 입력
#케이스의 수만큼 아래의 내용을 반복한다.
    N = int(input())
    I = list(map(int, input().split()))

    Average_ = (sum(I) // N) #소득의 평균값을 구하기
    cnt=0 #평균 이하의 소득을 가진 사람들의 수를 구하기 위한 변수
    for low_ in range(len(I)):
        if I[low_] <= Average_:
            cnt += 1
    print(f'#{case} {cnt}')