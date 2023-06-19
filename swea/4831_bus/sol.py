import sys
sys.stdin = open('input.txt')

# A도시는 전기버스를 운행하려고 한다. 
# 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해져 있어서, 중간에 충전기가 설치된 정류장을 만들기로 했다.

# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동하고, 
# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K가 정해져 있다.

# 충전기가 설치된 M개의 정류장 번호가 주어질 때, 
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그램을 만드시오.

# 만약 충전기 설치가 잘못되어 종점에 도착할 수 없는 경우는 0을 출력한다. 
# 출발지에는 항상 충전기가 설치되어 있지만 충전횟수에는 포함하지 않는다.

# 종점 N번째
# 충전시 이동가능 거리 K
# 충전기 O M개있고, 정류장 번호는 리스트로 주어짐 [] 

T = int(input()) # 3

for tc in range(1, T+1):
    list_R = list(map(int, (input().split()))) # 3, 10, 5

    recharge_center = list(map(int, input().split()))
    result = 0 
    here = 0 # 내위치
    
    K = list_R[0]
    N = list_R[1]
    M = list_R[2]

    # 다시 풀어보기

    print(f'#{tc} {result} \n')
