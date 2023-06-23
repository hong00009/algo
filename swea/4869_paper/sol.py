import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 5 #2 21 #3 85
T = int(input()) # 3

for tc in range(1, T+1):
    N = int(input()) // 10
    # 10, 20, 30, 40, 50, 60 이 input 되지만 index로 활용하기위해 10으로 나눈 값으로 활용


    memo = [0, 1, 3]

    while N >= len(memo): # 메모의 길이가 작으면 = > 아직 계산되지 않았으니 계산하겠다 ★★★
        p2 = memo[len(memo)-2]  # 2칸 전값
        p1 = memo[len(memo)-1]  # 1칸 전값

        now = p1 + p2 *2
        memo.append(now)

    print(memo)

