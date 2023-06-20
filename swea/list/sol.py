arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]

row_count = len(arr)  # 가로줄 덩어리 개수 =  4개 (열)
column_count = len(arr[0]) # 각각 덩어리의 길이 (행)

# print(row_count, column_count)

# for row in range(row_count):
#     for column in range(column_count):
#         print(row, column, arr[row][column])
# 123 456 789 101112

# for column in range(column_count):
#     for row in range(row_count):
#         print(row, column, arr[row][column])
# 14710 25811 36912


# for row in range(row_count):
#     for column in range(column_count):
#         #짝수행에서 역방향으로 탐색 (index 0,2,4 ...)
#         print(arr[row][column + (column_count-1 - 2*column) * (row % 2)])
# 123 654 789 121110
# row % 2 => 결과는 0 또는 1만 
# ( ) * 0 => 0이되므로   
# (column_count-1 - 2*column) * (row % 2) 은 수행하지 않고 arr[row][column] 그대로 출력
# ( ) * 1 => 총 길이 - column -1 > 역순으로 출력


# 델타 이동
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12],
]


# LRUD 순서 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# UDLR 순서
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1] 
# 상하좌우 순서는 상관없음, 4방향을 보는 것만 중요

# for x in range(len(arr)):  # 세로 길이만큼 for문수행
#     for y in range(len(arr[0])):
#         print(f'현재 위치는 {arr[x][y]}')

#         for i in range(4): # 0,1,2,3 > dx/dy의 index 순번돌기
#             temp_x = x + dx[i]
#             temp_y = y + dy[i]


            # try:
            #     print(f'{i} 방향에 있는 수는 {arr[temp_x][temp_y]}')
            # except:
            #     print(f'인덱스에러 : {temp_x} {temp_y}')


# 데이터 범위를 넘어 음수 -1 이되어도 
# [-1] 이 '끝에서 첫번째'라는 처리가 되어 에러없이 결과가 나오지만
# index 범위를 양수로 넘어서는 경우는 에러처리됨. 
# 양/음 초과 없도록 범위를 제한하여 처리하려면?
            # if 0 <= temp_x < len(arr)  and  0 <= temp_y < len(arr[0]):
            #     print(f'{i} 방향에 있는 수는 {arr[temp_x][temp_y]}')
            # else:
            #     print(f'벽 밖의 데이터 : {temp_x} {temp_y}')



# 4836 색칠하기
import sys
sys.stdin = open('input.txt')

# 결과 4, 5, 7
# T = int(input()) # 3

# for tc in range(1, T+1):
#     N = int(input()) # 사각형 개수 

#     for n in range(N):
        
#         i_1, j_1, i_2, j_2, color = map(int, input().split())
#         print('1) i,j: ', i_1,j_1)
#         print('2) i,j: ', i_2,j_2)
#         print('color1:', color)

#         arr = [[i_1, j_1], [i_2, j_2]]
#         # 받아온 좌표로 [ , ] 각각 생성하기
#         # [  [2,2], [4,4]  ]  / [  [3,3],  [6,6]  ]
#         print('만들어진 arr: ', arr,'\n')
    

#         row_count = len(arr)  # 가로줄 덩어리 개수 =  4개 (열)
#         column_count = len(arr[0]) # 각각 덩어리의 길이 (행)

        
#         for row in range(row_count):
#             for column in range(column_count):
                    
#                     # 답을 저장할 장소를 만들어둔다
#                 answer = []
#                 for i in range(5): #바깥쪽
#                     line = []
#                     for j in range(3): #안쪽
#                         line.append(0)
#                     answer.append(line)
#                 print('저장소:\n', answer)
#                 print('되나',len(answer), len(answer[0]))
                     
#                 for i in range(len(answer)):
#                     for j in range(len(answer[0])):
#                         # print('되나',len(answer), len(answer[0]))
#                         print(f'저장소[{i}][{j}]:', answer[i][j])

#             # 해당하는 범위의 값을 +1(빨강) 또는 +2(파랑) 더해줌
#             # 값이 3인곳을 출력 
        
#         print('-----\n')
#         # 00 / 01 / 10 / 11 순으로 접근함

# 집합의 원소가 n개
# 1 << n    // 모든 부분집합의 수  (2^n)
# 원소의 존재 유무를 2진수로 활용예정

# 부분집합
numbers = [2, 6, 3, 1]
# index    0  1  2  3

n = len(numbers) # 원수의 개수 n

# 1을 두번씩 곱해간다 n번만큼  => 2^4
for i in range(1<<n):
    # print(i)
    # print(bin(i), end=', ')
    for j in range(n):  # 원소의 수만큼 비트비교
        if i & (1<<j):
            print(numbers[j], end=', ')
    print()
# 1<<j   ==> 4개. 1, 10, 100, 1000
#  i   = > 2^n개. 0000. 0001. 0010. 0011.... 1111 
# i & (1<<j)   = > 인덱스번호판단
#  
# [공백]
# 2,  >0001
# 6,  >0010
# 2, 6, >0011
# 3,  >0100
# 2, 3,  >0101
# 6, 3, >0110
# 2, 6, 3,  >0111
# 1, > 1000
# 2, 1, 
# 6, 1,
# 2, 6, 1,
# 3, 1,
# 2, 3, 1,
# 6, 3, 1,
# 2, 6, 3, 1,