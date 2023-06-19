import sys
sys.stdin = open('input.txt')

T = int(input())  # => test case 3

# 데이터 가져오기
for tc in range(1,T+1):
    numbers = list(map(int, (input()))) # list화, 숫자 하나하나씩
    numbers.sort()
    is_babygin = 0

    result = 0
    print('numbers', numbers)
    counter = [0 for i in range(10)]
 
    for number in numbers:
        counter[number] += 1

    idx = 0
    while idx < len(counter):
        # 1. triplet 검증
        if counter[idx] >= 3:
            is_babygin += 1 # 3개이상이라고 검증되었으면 +1
            counter[idx] -= 3 # 해당인덱스값 3차감
            print('triplet')
            continue
        
        # 2. run 검증
        if idx < len(counter) -2:  # 마지막에서 2번째, 1번째 인덱스는 탐색할 필요가 없어 제외하기 
            if counter[idx] and counter[idx+1] and counter[idx+2]: # 해당 인덱스 값이 없으면 False 있으면 True
                is_babygin += 1
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                print('run')
                continue


        idx += 1

    print('counter', counter)

    if is_babygin == 2:
        result = True
    else:
        result = False

    print(f'#{tc} {result} \n')

