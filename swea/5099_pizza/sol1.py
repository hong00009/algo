import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 4  #2 8  #3 6
T = int(input()) # 3

for tc in range(1, T+1):
    
    # N : 화덕 크기   M : 피자 개수
    N, M  = map(int, input().split())
    
    # 피자에 올려진 치즈 개수
    cheeze = list(map(int, input().split()))

    # 피자 넘버링 과정
    before = [] # 기존 피자의 치즈 정보를 저장하기 위한 리스트
    for i in range(M): #피자 개수만큼 반복
        before.append([cheeze[i], i])
    # print(before)  # [치즈양, i번피자]  
    # (인덱스 편의를 위해 피자 넘버링을 0부터 시작, 실제 결과에서는 1 더해줘야함)

    # 비어있는 화덕 생성
    queue = [0]*N

    # 완성된 피자
    after = []

    # 피자가 완성될 때까지 반복해야함
    # 완성된 피자가 만들어야하는 피자 갯수랑 같아질때까지
    while len(after) != M:  # 완성된피자 != 피자개수면 계속 반복

        # 피자 넣는 규칙
        # 1) 화덕 입구에 공간이 비었다면 (꽉차면 못넣음)
        if queue[0] == 0:
            # 2) 넣을 피자가 있다면
            if len(before) != 0:
                # c : 기존 피자의 치즈값 / i : 기존 피자 번호 
                c, i = before.pop(0)
                # 3) 피자를 화덕에 넣는다
                queue.append([c,i])  # 화덕에 피자번호 포스트잇 붙여서 넣음 (끝에)
                # 4) 화덕을 돌린다
                queue.pop(0) 
            
            # 5) 넣을 피자가 없다면, 그냥 화덕을 돌려준다
            else: 
                queue.pop(0) # 0번째 자리를 빼고
                queue.append(0)   # (끝에) 0을 넣는다


        else: # 6) 입구에 이미 피자가 있음 (피자넣을공간X)
            # 피자 1개가 한바퀴를 돌아 처음위치로 왔다
            # 치즈 절반 감소
            queue[0][0] //= 2  # queue[0] 첫번째 인덱스 0값은 화덕입구

            # 7) 현재 다 완성된 피자인지 확인
            
            if queue[0][0] == 0: # 치즈 녹아서0, 완성되었다면
                # 8) 완성된 피자 꺼내기
                pizza = queue.pop(0)  
                
                # 9) 완성 리스트에 추가
                after.append(pizza[1]) # pizza[1] 은 포스트잇에 적힌 피자번호, 완성된 순서대로 번호만 after에 저장
            
                # 10) 더 넣을 피자 있는지 확인
                if len(before) !=0:
                    # (상단의 2번 코드와 동일함)
                    c, i = before.pop(0)
                    # 11) 피자를 화덕에 넣는다
                    queue.append([c,i])  # 화덕에 피자번호 포스트잇 붙여서 넣음 (끝에)

                else: # 12) 화덕을 돌린다
                    queue.append(0) 

            else:  #13) 아직 완성되지 않은 피자라면
                # 14) 아직 완성되지 않은 피자를 제일 뒤로 돌려주기
                pi = queue.pop(0)
                queue.append(pi)

    print(f'#{tc} {after[-1] + 1}') # 가장 마지막에 있는 피자의 인덱스 +1하여 출력