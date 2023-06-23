import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 731  #2 18641  #3 2412
T = int(input()) # 3

for tc in range(1, T+1):
    
    # N : 개수   M : M번반복
    N, M  = map(int, input().split())

    numbers  = list(map(int, input().split()))

    for _ in range(M) : # M번 반복
        deq = numbers.pop(0)  # 0번째 뽑아서
        numbers.append(deq) # 맨뒤에 넣기

    print(numbers[0])
