# 4836 색칠하기
import sys
sys.stdin = open('input.txt')

from pprint import pprint 
#2차원 배열 예쁘게 출력되도록 import

# 나와야 하는 결과 4, 5, 7
T = int(input()) # 3

for tc in range(1, T+1):
    N = int(input()) # 사각형 개수 

    # 2차원 배열 기본값 0으로 보드 생성
    board = [[0 for _ in range(10)] for _ in range(10)]
    # _ (언더스코어) 단순 반복작업위해 선언및활용은 했으나 
    # 그밖의 의미는 없을때 정하는 변수이름
    # pprint(board)
    for n in range(N):
        color_data = list(map(int, input().split()))
  
        #1. 반복문을 어디까지 돌려야하는지 범위 설정

        # 좌표 하나씩을 변수 하나씩으로 할당 (int형)

        left_top_x = color_data[0]
        left_top_y = color_data[1]
        right_bottom_x = color_data[2]
        right_bottom_y = color_data[3]

        color = color_data[4]

        for x in range(left_top_x, right_bottom_x+1):
            # 윗x좌표 ~ 아래x좌표 까지 반복
            for y in range(left_top_y, right_bottom_y+1):
                # 윗y좌표 ~ 아래y좌표 까지 반복
                board[x][y] += color

    pprint(board)


    count = 0
    for x in range(10):
        for y in range(10):
            if board[x][y] == 3:
                count += 1

    print(f'#{tc} {count}')
    print('\n')