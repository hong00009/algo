import sys
sys.stdin = open('input.txt')

T = 10
# 결과 
#1 67 ...

for _ in range(1, T+1):
    tc = int(input()) # 사다리번호
    ladder = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        # 도착지를 찾는 코드
        if ladder[99][i] == 2:
            x = i
            y = 99


    # y == 0 되는 시점  = > 제일 윗줄 도착, while문 종료
    while y > 0:
        # 현재 위치 기준, 좌/우를 체크   (x는 가로축 , y는 세로축)
        

        # 예외처리 분기문
        # 제일 오른쪽과 제일 왼쪽이 아니라면 > 좌우를 살펴보세요
        if x != 99 and x != 0:

            # 왼쪽 길이 있는 경우
            if ladder[y][x-1] == 1:
                ladder[y][x] = 0  # 내가 있던자리 0으로 설정
                x -= 1 # 왼쪽으로 이동
                continue

            # 오른쪽 길이 있는 경우
            if ladder[y][x+1] == 1:
                ladder[y][x] = 0 # 내가 있던자리 0으로 설정
                x += 1 # 오른쪽으로 이동
                continue

        # 제일 오른쪽이라면 > 왼쪽만 살펴보세요
        elif x == 99:
            # 왼쪽 길이 있는 경우
            if ladder[y][x-1] == 1:
                ladder[y][x] = 0  # 내가 있던자리 0으로 설정
                x -= 1 # 왼쪽으로 이동
                continue


        # 제일 왼쪽이라면 > 오른쪽만 살펴보세요
        elif x == 0:
            # 오른쪽 길이 있는 경우
            if ladder[y][x+1] == 1:
                ladder[y][x] = 0 # 내가 있던자리 0으로
                x += 1 # 오른쪽으로 이동
                continue


        # 왼쪽도 오른쪽도 길이 없는 경우
        ladder[y][x] = 0 # 내가 있던자리 0으로
        y -= 1 # 올라감

    result = x
    print(result)