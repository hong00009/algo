import sys
sys.stdin = open('input.txt')

T = 10
# 결과 
#1 691
#2 9092

sample = [0, 0, 3, 5, 2, 4, 9, 0, 6, 4, 0, 6, 0, 0]
# 샘플 답 6

for tc in range(1, T+1):
    N = int(input())
    Buildings = list(map(int,input().split()))
    # print(Buildings)

    
    result = 0
    for bd in range(N):
        
        me = Buildings[bd] # 기준점 me
        if me > 0: # 건물이 있는 곳만 검사

            f1 = me - Buildings[bd-1]
            f2 = me - Buildings[bd-2]
            b1 = me - Buildings[bd+1]
            b2 = me - Buildings[bd+2]

            if f1 > 0 and f2 > 0 and b1 > 0 and b2 > 0:
                result += min(f1,f2,b1,b2)
        else:
            continue
    print(f'{tc} {result}')

