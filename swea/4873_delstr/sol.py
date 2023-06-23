import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 1  #2 4  #3 11
T = int(input()) # 3

for tc in range(1, T+1):

    # V: 노드수  E : 간선수
    text = input()
    # print(text)

    stack = []

    for word in text:
        stack.append(word)
        if len(stack) == 1:
            continue
        # 마지막 1,2번째 글자가 같으면 2개 pop
        elif stack[-1] == stack[-2]:
            # stack[len(stack)-1], stack[len(stack)-2]
            stack.pop()
            stack.pop()

    print(f'#{tc} {len(stack)}')
           
