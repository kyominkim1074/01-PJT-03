import sys

sys.stdin = open("_최빈수구하기.txt")

t = int(input()) #테스트 케이스 반복시킬 수 있도록 변수 만들기
# 변수에 입력된 숫자만큼 반복시키기
for i in range(1, t+1): 
    test_case = input()
    num = list(map(int, input().split()))
    max_num = max(num)
    score = {} #딕셔너리를 적극 활용
    for i in num: # 리스트 안의 숫자들 중에
        if i in score: #만약 dict안에 해당 숫자(key)가 있으면(중복)
            score[i] += 1 # value에 +1해주고
        else: #아닐 경우
            score[i] = 1 #value값이 1이 된다.

    max_ = max(score.values()) #dict 안의 최대값을 새로운 변수에 대입하기.
    for k, v in score.items(): #key와 value의 값을 k, v에 넣어두고
        if v == max_: #변수v가 최대값(최빈수)과 같으면 출력
            print(f'#{test_case} {k}')