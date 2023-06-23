import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 8
#2 14
#3 9

def search(idx, visited):
    global result

    if idx >= N : # 모든 줄을 순회했을 때 result 출력
        print(result) 

    for i in range(0, N):
        if visited[i] == False:
            #방문하지 않은 False라면

            result.append(numbers[idx][i])
            # 내위치(idx) 줄 기준으로 i번째 항목을 골라 넣고
            visited[i] = True # 방문했다고 True로 바꿔줌

            search(idx +1, visited) # 재귀함수로 재호출, 다음인덱스
            # 0, FFF > 1, TFF > 2, TTF > 3, TTT 
            # 3이면 if문의 result 출력되고 함수 종결시켜 나가는데

            visited[i] = False
            # 나가면서 visited를 다시 False로 원복하고
            result.pop()
            # result 도 다시 비워줌


T = int(input()) # 3

for tc in range(1, T+1):
    
    N = int(input())
    numbers = []

    for _ in range(N):
        numbers.append(list(map(int, input().split())))


    visited = [False] * N
    result = []

    search(0, visited) # 우선 0번째 줄로 시작, FFF
    print('--------------')