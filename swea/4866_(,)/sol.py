import sys
sys.stdin = open('input.txt')

# 나와야 하는 결과 
#1 1 #2 1 #3 0
T = int(input()) # 3

for tc in range(1, T+1):
    text = input()

    s = []

    for char in text:
        if char == '(' or char == '{':
            s.append(char)
        elif char == ')':
            if s[-1] == '(':
                s.pop()
            else:
                s.append(char)
        elif char == '}':
            if s[-1] == '{':
                s.pop()
            else:
                s.append(char)
    if len(s) == 0 :
        print(1)
    else:
        print(0)