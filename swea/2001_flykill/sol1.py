import sys
sys.stdin = open('input.txt')

from pprint import pprint

T = int(input()) # 10
for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [ list(map(int, input().split())) for i in range(N)] # ★ list comprehension
    # print(matrix)

    result = 0

    # N-M+1 => 기준점이 반복문을 돌 수 있는 범위
    for i in range(N-M+1): # 전체 범위 안에서 어디까지 반복 돌릴지 기준점 설정
        for j in range(N-M+1):
            # print(matrix[i][j]) # => 기준점

            # 파리채 크기(M) 만큼 반복을 돌면서 총합
            temp_total = 0
            for col in range(M) :
                for row in range(M):
                    # matrix[i+col][j+row]  # 내위치 기준 파리채만큼
                    temp_total += matrix[i+col][j+row]


            if result < temp_total:
                result = temp_total
    print(result)