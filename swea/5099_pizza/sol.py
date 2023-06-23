import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 4  #2 8  #3 6
T = int(input()) # 3

for tc in range(1, T+1):
    
    # N : 화덕의 크기(동시굽기수)   M : M개의 피자
    N, M  = map(int, input().split())

    # 피자 위 치즈의 양
    pizzas  = list(map(int, input().split()))

    print('화덕의 크기: ', N, '피자 개수:',M)
    print(pizzas)

    Q = []
    
    # 화덕크기N개만큼 화덕에 피자를 넣는다

    while True:
        
        for i in pizzas:
            if len(Q) < N: # 화덕Q의 동시굽기개수까지 append
                Q.append(i)
            
            elif len(Q) == N : # 화덕이 꽉차면
                print('피자 다 넣음',Q)
                Q[0] = Q[0] // 2 # 한바퀴 돈 피자 치즈 절반 녹음
                print('치즈녹음',Q)
                if Q[0] !=0 :   # 절반녹은게 0이 아니면 위치이동
                    temp = Q.pop(0)
                    Q.append(temp)
                    print('위치이동',Q)
                elif Q[0] == 0:  #0이면 꺼내고 새피자 넣음
                    Q[0] = i
            else:
                break
        
        
    # 입구에서 피자를 볼 때, 치즈의 양이 0이면 피자를 꺼낸다
    # 꺼낸 빈 자리에 다음 피자를 넣어준다
