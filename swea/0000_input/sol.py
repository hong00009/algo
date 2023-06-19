import sys
sys.stdin = open('input.txt')

# 숫자 데이터 하나 받아오기
N = int(input())
result = '홀수' if N%2 else '짝수'
print(f'#1 {result}')


# 리스트형태 데이터 받아오기
numbers = list(map(int, input().split()))
# split: 문자열 띄어쓰기 단위로 쪼개서 리스트화됨
# map : int형으로 변환
# list : list형으로 변환
result = sum(numbers)
print(f'#2 {result}')


# 2차원 리스트형태 데이터 받아오기
number_list = []
N = int(input())
for i in range(N):
    numbers = list(map(int, input().split()))
    number_list.append(numbers)

result = number_list[1][1]
print(f'#3 {result}')