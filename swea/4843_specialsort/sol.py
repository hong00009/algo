import sys
sys.stdin = open('input.txt')

T = int(input()) 

for tc in range(1, T+1):
    N = int(input()) # 정수 개수 , 리스트 길이

    numbers = list(map(int, input().split()))
    # print(N, numbers)

    # .sort()를 쓸수도 있음

    for i in range(len(numbers)-1, 0, -1): #전에 배운 버블정렬
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    result = []
    # 큰수5, 작은수5 나눠서 넣기

    for i in range(5):
        # 뒤에서부터 숫자를 불러와서 result에 저장
        result.append(numbers[-i-1]) # 가장 마지막 수, 역순
        
        #앞에서부터 숫자를 불러와서 result에 저장
        result.append(numbers[i])
                      
    result = ' '.join(map(str,result))
        
    # print(result)

    print(f'#{tc} {result}')