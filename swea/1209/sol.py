import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input()) 

    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
        # 100줄 읽어오기
    
    sum_a = []
    sum_b = []
 
    for i in range(100):
        sum_a.append(sum(arr[i])) # a 가로
        
        summ = 0
        for j in range(100): # b 세로
            summ += arr[j][i]
            # print(f'arr[{i}][{j}]')
        sum_b.append(summ)

        sum_c = 0
         # c 대각선1
        sum_c += arr[i][i]

        sum_d = 0
        # d 대각선2
        sum_d += arr[99-i][i]

    m_a = max(sum_a)
    m_b = max(sum_b)
    print(f'#{tc} {max(m_a, m_b, sum_c, sum_d)}')

