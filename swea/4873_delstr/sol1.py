import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 1  #2 4  #3 11
T = int(input()) # 3

for tc in range(1, T+1):
    string = input()
    stack = []
    for char in string:
        #스택이 비어있는 경우
        if len(stack) ==0:
            stack.append(char)

        #스택에 데이터가 있는 경우
        else:
            #스택의 제일 마지막 데이터가 지금 반복문을 돌리고 있는 데이터와 일치하면
            if stack[-1] ==char:
                stack.pop()

            #일치하지 않는다면
            else:
                stack.append(char)
                
    print(stack)