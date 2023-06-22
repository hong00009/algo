import sys
sys.stdin = open('input.txt')

T = 10
# 결과 
#1 691
#2 9092

for tc in range(1, T+1):

    N = int(input()) # 빌딩 수
    buliding_list = list(map(int,input().split()))
    
    total = 0

    # 1 내가 제일큰가 / 2 나와 다른 제일 큰 값의 차이

    # 모든 건물들을 기준으로 반복
    for i in range(N):
        now = buliding_list[i] # 현재 위치
        
        # 지금 나의 위치가 0이라면 비교할 필요X 다음 건물로 스킵
        if now == 0: # 건물 없으면 스킵
            continue
        else:
            # 양옆 * 2개의 건물을 비교
            idx = [-2, -1, 1, 2] # 내기준 양옆2칸씩 접근할 인덱스
            max_tall = 0
            
            # 비교 건물중 가장 큰 건물을 max_tall에 저장
            for j in range(4):
                comp = buliding_list[i + idx[j]]
                if max_tall < comp:
                    max_tall = comp

            if now > max_tall:
                view = now - max_tall
                total += view
    print(f'#{tc} {total}')



        
