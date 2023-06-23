import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 8
#2 14
#3 9

def search(idx, visite, SUM):
    global MIN

    if idx >= N : # 모든 줄을 순회했으면 SUM과 MIN 값 비교하여 MIN을 최소값으로 설정 후 함수종결
        if SUM < MIN:
            MIN = SUM #
        return
            
    if SUM > MIN: # MIN보다 SUM이 더 크면 함수종결
        return 

    for i in range(0, N):
        if visited[i] == False:
            #방문하지 않은 False라면

            SUM += numbers[idx][i] # SUM에 더해주고
            visited[i] = True # 방문했다고 True로 바꿔줌

            search(idx +1, visited, SUM) # 재귀함수로 재호출, 다음인덱스 확인
            # 0, FFF > 1, TFF > 2, TTF > 3, TTT 
            # 3이면 상단의 if문(MIN과 SUM크기비교) 확인하고 함수 종결시켜 나가는데

            visited[i] = False
            # 나가면서 visited를 다시 False로 원복하고
            SUM -= numbers[idx][i]
            # SUM도 원복


T = int(input()) # 3

for tc in range(1, T+1):
    
    N = int(input())
    numbers = []

    for _ in range(N):
        numbers.append(list(map(int, input().split())))


    visited = [False] * N
    MIN = 99999999
    SUM = 0


    search(0, visited, SUM) # 현재 더한값 SUM을 계속 들고감
    print(MIN)
    print('--------------')