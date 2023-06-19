import sys
sys.stdin = open('input.txt')

T = int(input()) 

for tc in range(1, T+1):
    N, M = map(int, input().split())

    numbers = list(map(int, input().split()))

    # min_number = 999999 # 1. 그냥 제일 커보이는 숫자 정하기
    min_number = sum(numbers) # 2. 모든수의 합으로 정하기
    # min_number = 999999 # 3. 문제에서 제한된 제일 큰수로 정하기
    max_number = 0

    # 구간합의 시작점을 찾는 i
    for i in range(N-M+1):
        # 시작점을 기준으로 오른쪽 M개의 합
        total = 0

        for j in range(M): #내기준 M번까지반복
            total += numbers[i+j]

        # total과 min / max 값을 비교해가며 저장
        if total < min_number:
            min_number = total
        if total > max_number:
            max_number = total

    result = max_number - min_number

    print(f'#{tc} {result}')