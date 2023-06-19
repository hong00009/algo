import sys
sys.stdin = open('input.txt')

T = int(input()) # 3개의 테스트케이스
# N개의 정수가 들어있는 배열에서 
# 이웃한 M개의 합을 계산
result = 0
now = 0  # 내위치 인덱스값
count_num = [] # 계산값을 넣을 곳

# 현재 위치 기준 (now + now+1 + now+2 + ... )을 계산한다 
# 계산한 결과를 저장한다
# 제일작은값 제일큰값의 차를 구한다


for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N 정수의 개수 / 10 ≤ N ≤ 100
    # M 구간의 개수 / 2 ≤ M ＜ N 

    list_num = list(map(int, input().split()))
    # 정수 N 개수 만큼 더해야됨
    # 6, 9, 12, 15 ...
    # M - N + 1 까지 반복

    # 다시 풀어보기

    print(f'#{tc} {result}')