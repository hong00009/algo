import sys
sys.stdin = open('input.txt')

T = int(input()) # 3개의 테스트케이스

for tc in range(1, T+1):
    # K 최대 이동가능한 정류장 수
    # N 종점
    # M 충전기가 설치된 정류장 수
    K, N, M = map(int, input().split())

    bus_stop = list(map(int, input().split()))  # [1 3 5 7 9]
    cnt = 0 
    now = 0 # 내 위치

    # 1. 내가 현재 갈수 있는 최대거리 확인
    # 2. 그곳 기준으로 제일 가까운 충전소 탐색(운행 반대방향)
    # 3. 종점 도착시 (충전 필요없이) 종결
    
    # ★ 충전할 필요 없이 바로 도착하는 경우를 if로 우선설정
    if K >= N:
        cnt = 0
    # 충전하면서 지나가야 할 때
    else:
        # 버스가 아직 종점에 도착하지 않았다면 계속 해서 반복
        while now < N:  # 내위치 < 종점
            # ★★현재 위치(now)에서 최대로 갈 수 있는 정류장 범위(now+K)를 찾는다
            # range : '최대거리(now+K)'부터, '현재위치now'까지, 역순으로 반복
            for i in range(now+K, now, -1): 
                # 1. 최대 범위가 종점을 넘는 경우 / 현재위치 = 종점, 종결
                if i >= N:
                    now = N
                    break
                # 2. 최대 범위가 종점을 아직 넘지 않는 경우
                if i in bus_stop:
                    # 가장 뒤에있는 충전소로 이동
                    now = i
                    # 충전 후 이동하여 카운트 증가
                    cnt += 1
                    break # 충전소 만났으니 더이상 앞쪽 충전소 찾지말고 종결


            # 현재 위치에서 최대 이동가능 거리를 찾았지만, 그 사이에 충전소가 없다 >> 도착 불가능
            else:
                cnt = 0
                now = N # 상위 while문 종료를 위해 내위치를 종점으로 설정하여 종결
    print(f'#{tc} {cnt}')
    print(K, N, M, bus_stop)


