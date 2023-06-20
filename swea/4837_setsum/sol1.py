import sys
sys.stdin = open('input.txt')


# 나와야 하는 결과 1, 0, 0
T = int(input()) # 3

for tc in range(1, T+1):

    # 원소수N, 부분집합의합 K
    N, K = map(int, input().split())

    arr = list(range(1,13))
    # A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    #  idx 0  1  2  3  4  5  6  7  8  9  10  11
    # 모든 부분집합의 개수는 2^12개
    count = 0
    
    for i in range(1 << len(arr)):
        result = [] # 결과저장공간
        for j in range(len(arr)):
            if i & (1 << j): 
                # i    0000, 0001, 0002 ~ 111(12자리)
                # i << j     1, 10, 100, 1000 ....
                # i & (i<<j)  0000 & 1, 10, 1000 ...
                #             0001 & 1, 10, 1000 ...
                result.append(arr[j])
        # print(result) > 부분집합의 경우의수 2^12개 모두 만들어 출력함

        if len(result)  == N and sum(result) == K:
            count += 1
        # 길이가 N 이고 합산이 K 와 일치하는 경우만 검출

    print(f'#{tc} {count}')