import sys
sys.stdin = open('input.txt')

from pprint import pprint
# 나와야 하는 결과 
#1 1 #2 1 #3 1
T = int(input()) # 3

for tc in range(1, T+1):

    # V: 노드수  E : 간선수
    V, E = list(map(int, (input().split()) ))
                    
    # 비어있는 값으로 초기화하여 만들어두기
    nodes = [ [0] * (V+1) for _ in range(V+1)]
    # 0번째 인덱스는 실제로 쓰지 않지만, 각 노드와 인덱스번호의 싱크를 맞추기 위해 넣어둠
    # 6번째 인덱스, 6노드    

    for line in range(E): # E개의 노드 가져오기
        start, end = list(map(int, input().split()))
        nodes[start][end] = 1 # 예 , 1>3 이동 가능
        nodes[end][start] = 1 # 예 , 3>1 이동 가능 (양방향이동가능표기)

    # pprint(nodes)

    # S  확인해야하는 출발노드  
    # G  연결되어있음을 확인해야하는 도착노드
    S, G = list(map(int, input().split())) 


    # 내가 방문했던 기록을 남기는 체크리스트
    # False 값으로 초기화
    check_list = [False] * (V+1) 

    # 거리 계산을 위한 리스트
    distance = [0] * (V+1)
    
    # BFS 처리용 queue 
    queue = []

    # v : 현재위치 v 부터 시작
    v = S
    check_list[v] = True  # 내위치 방문기록 True , queue 에 넣기
    queue.append(v)

    reuslt = 0
    while len(queue): # 1) queue에 하나라도 데이터가 있다면(1) 반복, 아무것도 없으면(0) break
        # 최초에는 현재 위치 v를 넣어놔서 len 1임
        # while 0이되는 조건 > 갈수있는 곳을 다 방문했을때

        v = queue.pop(0) # 2) 큐 빼기

        # 3) 현재 나의 노드(v)와 연결된 노드(w)를 탐색
        for w in range(V+1):
            if nodes[v][w] == 1 : #4) v와 w가 연결되어있다면
                # print(queue)
                 # 5) 아직 방문을 안했다면
                if check_list[w] == False:
                     
                     # 6)연결된 노드(w)를 방문 처리
                    check_list[w] = True

                    # 7) 현재깊이에서 1 증가시킨후 다음위치의 깊이를 저장
                    distance[w] = distance[v] +1
                    queue.append(w)
    print(distance)
    print(distance[G])
