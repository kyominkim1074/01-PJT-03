import sys

sys.stdin = open("_암호문1.txt")

for t in range(1, 11):
    N = int(input()) #원본 암호문의 길이
    Pass = list(map(int, input().split())) # 원본 암호문
    Command_N = int(input()) #명령어 개수
    Com_ = list(input().split())
    
    print(f'#{t}', end=' ') # 테스트 케이스 공백을 포함해서 출력
    
    for i in range(len(Com_)): #암호의 개수만큼 반복한다.
        if Com_[i] == 'I': #명령어의 i값이 I인 경우
            ins_i = int(Com_[i+1]) #숫자를 삽입할 위치
            ins_n = int(Com_[i+2]) #삽입할 숫자의 개수
            
            for j in range(ins_n): #삽입할 숫자의 개수 만큼
                #원본 암호문 첫번째 다음 부터 차례로 insert시킴
                Pass.insert(ins_i + j, Com_[i+3+j])
                
    for r in range(10): # 최종 수정된 암호문의 처음 10개를 출력
        print(Pass[r], end=' ')
    print()