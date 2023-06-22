import sys
sys.stdin = open('input.txt')

from pprint import pprint

T = int(input()) # 10
for tc in range(1, T+1):

    # N = N * N 전체범위
    # M = M * M 파리채 범위
    N, M = map(int,input().split())
    arr = []
    arr2 = []
    for _ in range(N):
        arr.append(input().split())

    for row in range(N-M+1): # 파리채가 때릴 수 있는 범위까지 탐색
        # 가로 한줄
        for i in range(N-M+1):             
            for j in range(M):
                print('??',arr[row+j][i+j])
    # print('arr2', arr2)
    # print(max(arr2))
    print('-----')



        