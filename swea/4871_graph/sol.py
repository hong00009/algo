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

        nodes[start][end] = 1

    # pprint(nodes)

    # S  확인해야하는 출발노드  
    # G  연결되어있음을 확인해야하는 도착노드
    S, G = list(map(int, input().split())) 

    # dif를 하기 위해 과거를 기록하는 stack 생성
    stack = []

    # 내가 방문했던 기록을 남기는 체크리스트
    # False 값으로 초기화
    check_list = [False] * (V+1) 

    # v : 현재위치
    v = S
    check_list[v] = True  # 내위치 방문기록 True , stack에 쌓음
    stack.append(v)

    reuslt = 0
    while len(stack): # stack에 하나라도 데이터가 있다면(1) 반복, 아무것도 없으면(0) break
        # while 0이되는 조건 > 갈수있는 곳을 다 방문했을때

        # 현재 나의 노드(v)와 연결된 노드(w)를 탐색
        for w in range(V+1):
            if nodes[v][w] == 1 : # v와 w가 연결되어있다면
                print(stack)
                 # 아직 방문을 안했다면
                if not check_list[w]:
                     
                     # 연결된 노드(w)를 방문 처리
                    check_list[w] = True

                     # 나의 노드(v)를 stack에 push
                    stack.append(v)

                     # 현재위치를 이동 (v => w)
                    v = w

                     # 경로에 목적지가 있으면 저장
                    if w == G: 
                        result = 1

                    break # for문 종료
            
        else:  # for 문의 else
            # 탐색할 것이 아무것도 없으면
            v = stack.pop() # stack에서 꺼낸 것을 v에 저장

    print(f'#{tc} {result}')