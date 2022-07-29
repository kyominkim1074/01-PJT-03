import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
# 리스트화 시킨 문자열을 전체적으로 뒤집은 다음에 글자 하나하나씩 뒤집도록 한다.
for case in range(1, T+1): # 케이스의 개수 만큼 반복한다.
    st = list(input()) #입력한 문자열을 리스트화 시킨다.
    st.reverse() #리스트의 내용을 뒤집는다.
    for i in range(len(st)): # 리스트의 범위 숫자 만큼 각각 알파벳을 뒤집도록 반복한다.
        if st[i] == 'b':
            st[i] = 'd'
        elif st[i] == 'd':
            st[i] = 'b'
        elif st[i] == 'q':
            st[i] = 'p'
        elif st[i] == 'p':
            st[i] = 'q'
    print('#'+str(case), ''.join(st))