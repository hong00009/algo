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
    # N x N 정사각형 크기의 글자판
    # M 회문의 길이

    arr = []
    arr2 = [0]*N
    arr3 = [0]*N
    arr4 = []

    for _ in range(N):
        arr.append(input())
    pprint(arr)
    
    for i in range(N):
        for j in range(N):
            v = M-1-j
            
            if arr[i][j] == arr[i][v]:
                arr2[i] +=1
    
            if arr[j][i] == arr[v][i]:
                arr3[i] +=1

    print(f' arr2 : {arr2}, arr3 : {arr3}')

    for i in range(N):
        a = M-1
        if arr2[i] == M:
            print(f'#{tc} {arr[i]}') 

        if arr3[i] == M:
            while a > 0:
                arr4.append(arr[a][i])     
                a -= 1   
            print(f'#{tc} {"".join(arr4)}')