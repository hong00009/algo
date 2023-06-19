import sys
sys.stdin = open('input.txt')

T = int(input()) # 3개의 테스트케이스

for tc in range(1, T+1):
    N = int(input()) # 카드 장수 N개
    numbers = list(map(int, input())) #49679 

    count_list = [0 for i in range(10)]

    # 숫자만날때마다 1씩 증가
    for number in numbers:
        count_list[number] += 1

    max_count = 0

    # enumerate 인덱스, 값 동시 추출하여 사용
    for idx, count in enumerate(count_list): 
        if max_count <= count:
            result = idx
            max_count = count   

    print(f'#{tc} {result} {max_count}')    

