import sys
sys.stdin = open('input.txt')

from pprint import pprint
# 나와야 하는 결과 
#1 JAEZNNZEAJ
#2 MWOIVVIOWM
#3 TLMMHOOOHMMLT
T = int(input()) # 3
for tc in range(1, T+1):
    N, M = map(int,input().split())
    # N : N x N 보드
    # M : 회문의 길이

    string_map = []
    for str in range(N):
        string_map.append(input())

    result = []

    # 가로
    for row in range(N): # 가로 한줄씩 반복실행
        # print(string_map[row]) > 한줄씩 나옴
        # 회문의 시작점 설정하고 시작점만 반복  / 시작점 : N-M+1
        for i in range(N - M + 1):
            # print(string_map[row][i])  / 글자하나씩

            # 회문인지 확인
            for j in range(M//2):  # 앞뒤/뒤앞 중복검수하므로 반으로 줄임
                # front : 앞글자
                f = string_map[row][i+j]

                # back : 뒷글자
                b = string_map[row][i+M-j-1]

                # 앞뒤가 똑같다면
                if f == b:
                    flag = True  # 회문표시 flag

                #앞뒤가 다르다면
                else:  # for문 돌다가 하나라도 다르다면 False로 처리
                    flag  False
                    break # 회문확인 for문 탈출 / 다음 시작점으로

            if flag: # flag True인경우
                for k in range(M):
                    result += string_map[row][i+k]

    # 세로
   