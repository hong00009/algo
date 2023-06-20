import sys
sys.stdin = open('input.txt')

T = int(input()) 

for tc in range(1, T+1):
    P, A, B = map(int, input().split())

    # P : 책의 장수(마지막페이지)
    # A : A의 목적 페이지
    # B : B의 목적 페이지

    count_a = 1
    left = 1
    right = P

    while True:
        middle = int((left+right)/2)

        # 목적 페이지가 가운데보다 왼쪽에 있는 경우
        if A < middle:
            right = middle

        # 목적 페이지가 가운데보다 오른쪽에 있는 경우
        elif middle < A:
            left = middle
        # 둘다 아니라면 목적 페이지에 도착
        else:
            break

        count_a += 1


    count_b = 1
    left = 1
    right = P

    while True:
        middle = int((left+right)/2)

        # 목적 페이지가 가운데보다 왼쪽에 있는 경우
        if B < middle:
            right = middle

        # 목적 페이지가 가운데보다 오른쪽에 있는 경우
        elif middle < B:
            left = middle
        # 둘다 아니라면 목적 페이지에 도착
        else:
            break

        count_b += 1
    # print(count_a, count_b)
    if count_a < count_b:
        winner = 'A'
    elif count_a > count_b:
        winner = 'B'
    else:
        winner = 0

    print(f'#{tc} {winner}')