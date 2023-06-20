import sys
sys.stdin = open('input.txt')


# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1<=T<=50
# 테스트 케이스 별로 책의 전체 쪽 수 P, 
# A, B가 찾을 쪽 번호 Pa, Pb가 차례로 주어진다. 1<= P, Pa, Pb <=1000

# 나와야 하는 결과 A, 0, A
T = int(input()) # 3

for tc in range(1, T+1):

    # P 페이지 전체수, Pa a가 찾을 페이지, Pb b가 찾을 페이지
    P, Pa, Pb = map(int, input().split())

    left_a = 1
    left_b = 1
    answer = 0
    count_a = 0
    count_b = 0
    right_a = P
    right_b = P
    while answer != Pa:
        center = int((left_a+right_a)/2)

        if Pa ==  center:
            answer = Pa
        elif Pa > center:
            left_a = center
        elif Pa < center:
            right_a = center
        count_a += 1
        # print('A:',left_a,center,right_a,count_a)
        

    while answer != Pb:
        center = int((left_b+right_b)/2)

        if Pb ==  center:
            answer = Pb
        elif Pb > center:
            left_b = center
        elif Pb < center:
            right_b = center
        count_b += 1
        # print('B:',left_b,center,right_b,count_a)

    if count_a < count_b:
        win = 'A'
    elif count_a > count_b:
        win = 'B'
    elif count_a == count_b:
        win = 0
    print(f'#{tc} {win}')