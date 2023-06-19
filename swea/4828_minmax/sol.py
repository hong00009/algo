import sys
sys.stdin = open('input.txt')

# input 값
# 3
# 5
# 477162 658880 751280 927930 297191
# 5
# 565469 851600 460874 148692 111090
# 10
# 784386 279993 982220 996285 614710 992232 195265 359810 919192 158175

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    numbers = list(map(int, input().split()))
    # print(N, numbers)

    min_number = 1000000 # 문제에서 설정한 최댓값과 최소값을 초기값으로 할당
    max_number = 1
    # min_number = numbers[0] # 만약 문제에 최대/최소 값이 없다면 가장 첫번쨰값을 최대/최소 초기값으로 할당

    for number in numbers:
        if min_number > number:
            min_number = number
        if max_number < number:
            max_number = number

    result = max_number - min_number

    print(f'#{tc} {result}')