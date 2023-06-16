# 100문제 중 42 

# 배열 두배만들기
def solution(numbers):
            answer = []
            for i in numbers:
                answer.append(i*2)
            return answer

# print(solution([1, 2, 3, 4, 5]))
# print(solution([1, 2, 100, -99, 1, 2, 3]))


# 아이스 아메리카노
def solution(money):
    a, b = divmod(money, 5500)
    answer = [a, b]
    return answer
# print(solution(5500))
# print(solution(15000))


# 7의 개수
def solution(array):
    answer = 0
    string_value = str(array)
    answer = string_value.count('7')
    return answer
# print(solution([7, 77, 17]))
# print(solution([10, 29]))
# print(solution([77777, 37971]))


# 대소문자 바꿔서 출력하기
str1 = 'aBcDeFg'
result=''
for i in range(len(str1)):
    if str1[i].isupper():
          a = str1[i].lower()
          result += a
    elif str1[i].islower():
        a = str1[i].upper()
        result += a
print(result)

# 다른사람 코드
#print('aBcDeFg'.swapcase())
# ?????????? 벼리별 코드가 다있네

# 문자열 돌리기 (한줄씩 자르기)
#print('\n'.join(str1))

# 문자열 겹쳐쓰기
def solution(my_string, overwrite_string, s):
    pront = my_string[0:s] + overwrite_string
    answer = pront
    if len(my_string) > len(pront):
        back = my_string[len(pront):]  
        answer = pront + back
    return answer
# 붙인 부분이 원본보다 짧으면, 뒷부분을 구해서 붙여줬음

# print(solution("He11oWor1d", "lloWorl", 2))
# print(solution("Program29b8UYP", "merS123", 7))
# print(solution("abcabcabcabc", "OOO", 3))

# 다른사람 코드 
def solution(my_string, overwrite_string, s):
    return my_string[:s] + overwrite_string + my_string[s + len(overwrite_string):]


# 문자열 섞기
def solution(str1,str2):
    answer = ''
    for i in range(len(str1)):
         answer = answer+ str1[i] + str2[i]
    return answer
print(solution("aaaaa", "bbbbb"))
print(solution("12345", "abcde"))

# 문자 리스트를 문자열로 변환하기
def solution(arr):
    answer = ''
    for i in range(len(arr)):
        answer += arr[i]
    return answer

print(solution(["a","b","c"]))
print(solution(["a","b","c",'d','e','f','g']))

# 다른사람 코드 1
def solution(arr):
    return ''.join(arr)

# 다른사람 코드 2
# 굳이 for문을 리스트의 index 숫자값으로 처리하지 않고, 리스트 그대로 사용
def solution(arr):
    answer = ''
    for a in arr:
        answer += a 
    return answer

# 다른 사람 코드 3 /람다
solution = lambda arr: ''.join(arr)

# 더 크게 합치기
def solution(a, b):
    answer = 0
    a1 = str(a)+str(b)
    a2 = str(b)+str(a)
    if int(a1) < int(a2):
         answer = a2
    else:
         answer = a1
    return int(answer)
print(solution(9, 91))
print(solution(89, 8))

# 다른사람 코드
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

#두 수의 연산값 비교하기
def solution(a, b):
    answer = 0
    a1 = str(a)+str(b)
    a2 = 2 * a * b
    if int(a1) < a2 :
         answer = a2
    else:
         answer = a1
    return int(answer)

print(solution(2, 91))
print(solution(91, 2))

# 다른사람 코드
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)

# n의 배수 (배수이면 1을, 배수가 아니라면 0을 return)
def solution(num, n):
    if num % n == 0:
         return 1
    else :
         return 0

# 다른사람 코드 
def solution(num, n):
    return int(not(num % n))

# 공배수 / 공배수면 1, 아니면 0 리턴
def solution(number, n, m):
    if (number % n == 0) & (number % m == 0):
        return 1
    else:
         return 0
    
# 홀짝에 따라 다른 값 반환하기
# 양의 정수 n
# 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return 
# 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return 

def solution(n):
    answer1 = 1
    answer2 = 0
    if n % 2 == 1 :
         for i in range(0,int(n/2+1)):
              # 1+3+5+7 
              answer1 = answer1 + 2*i
         return answer1
    else :
         for i in range(0, int(n/2)):
              answer2 = answer2 + i**2
         return answer2
# print(solution(7)) #16
# print(solution(10)) #220

# 짝수의 합
def solution(n):
    answer = 0
    for i in range(0, n+1, 2):
        answer += i
    return answer
print(solution(10)) #30
print(solution(4)) #6
print(solution(7)) #12

# 배열의 평균값
def solution(numbers):
    answer = 0
    answer = sum(numbers)/len(numbers)
    return answer

# 양꼬치
def solution(n, k):
    answer = 0
    yang = n * 12000
    drink = k * 2000
    sale = (n//10) * 2000
    answer = yang + drink - sale
    return answer
print(solution(10, 3)) #124000
print(solution(64, 6)) #768000
print(solution(30, 30)) 
print(solution(1, 1)) 

# 배열 뒤집기
def solution(num_list):
    num_list.reverse()
    answer = num_list
    return answer
print(solution([1, 2, 3, 4, 5])) 

# 다른사람 코드
def solution(num_list):
    return num_list[::-1]

# 짝수 홀수 개수
def solution(num_list):
    answer = []
    a = 0
    b = 0
    for i in num_list:
        if i % 2 == 0:
            a += 1
        else:
            b += 1
    answer = [a, b]
    return answer
print(solution([1, 2, 3, 4, 5])) # [2, 3]
print(solution([1, 3, 5, 7])) # [0, 4]

# 중복된 숫자 개수
def solution(array, n):
    answer = 0
    answer = array.count(n)
    return answer
print(solution([1, 1, 2, 3, 4, 5], 1)) # 2
print(solution([0, 2, 3, 4], 1)) # 0

#  최댓값 만들기 (1)
def solution(numbers):
    answer = 0
    numbers.sort()
    answer = numbers[-1] * numbers[-2]
    return answer

print(solution([1, 2, 3, 4, 5])) # 20
print(solution([0, 31, 24, 10, 1, 9])) # 744


# 문자열 뒤집기 ★ 문자열[start : stop : step]  / -1은 역순
def solution(my_string):
    answer = my_string[::-1]
    return answer
print(solution("jaron"))#	"noraj"

# 피자 나눠 먹기 (3)
def solution(slice, n):
    answer = 0
    a, b = (divmod(n,slice))
    if b > 0:
        answer = a + 1
    else:
        answer = a
    return answer
# 한판을 2조각~ 10조각까지만 나눔
print(solution(7, 10)) # 2
print(solution(4, 12)) # 3


# 문자열안에 문자열
def solution(str1, str2):
    answer = str1.count(str2)
    if answer > 0:
        return 1
    else:
        return 2
print(solution("ab6CDE443fgh22iJKlmn1o","6CD")) # 1
print(solution("ppprrrogrammers","pppp")) #2
print(solution("AbcAbcA","AAA")) #2

# 다른사람 코드
def solution(str1, str2):
    return 1 if str2 in str1 else 2
#    return 1 
#  if str2 in str1  / str2가 str1에 있다면 return 1
#   else 2          / 아니면 return 2

# 숨어있는 숫자의 덧셈 (1)
def solution(my_string):
    answer = 0
    print(my_string)
    for i in my_string:
        if i.isnumeric() :
            answer += int(i)
    return answer
print(solution("aAb1B2cC34oOp")) # 10
print(solution("1a2b3c4d123")) # 16

# 중앙값 구하기
def solution(array):
    answer = 0
    array.sort()
    answer = array[len(array)//2]
    return answer
print(solution([1, 2, 7, 10, 11])) # 7
print(solution([9, -1, 0])) # 0

# 점의 위치 구하기
def solution(dot):
    answer = 0
    if dot[0] > 0 and dot[1] > 0:
        answer = 1
    elif dot[0] < 0 and dot[1] > 0:
        answer = 2
    elif dot[0] < 0 and dot[1] < 0:
        answer  = 3 
    elif dot[0] > 0 and dot[1] < 0:
        answer = 4
    return answer
print(solution([2,4])) # 1
print(solution([-7,9])) # 2


# 삼각형의 완성조건 (1)
# 가장 긴 변의 길이는 다른 두 변의 길이의 합보다 작아야 합니다.
# 삼각형 가능 1, 삼각형 불가 2

def solution(sides):
    sides.sort()
    if sides[-1] < sides[0] + sides[1]:
        return 1
    else:
        return 2

print(solution([1, 2, 3])) # 2
print(solution([3, 6, 2])) # 2
print(solution([199, 72, 222])) # 1

# 머쓱이보다 키 큰 사람
def solution(array, height):
    answer = 0
    for i in array:
        if i > height:
            answer += 1
    return answer
print(solution([149, 180, 192, 170], 167)) # 3
print(solution([180, 120, 140], 190)) # 0

# 배열 원소의 길이
def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

print(solution(["We", "are", "the", "world!"])) # [2, 3, 3, 6]
print(solution(["I", "Love", "Programmers."])) # [1, 4, 12]

# 다른사람 코드
def solution(strlist):
    answer = list(map(len, strlist))
    return answer

# 편지
def solution(message):
    return len(message) * 2

print(solution("happy birthday!")) # 30
print(solution("I love you~")) # 20


# 배열의 유사도
def solution(s1, s2):
    answer = 0
    print(s1, s2)
    for i in s1:
        for j in s2:
            if i == j:
                answer = answer + 1
    return answer

print(solution(["a", "b", "c"], ["com", "b", "d", "p", "c"] )) # 2
print(solution(["n", "omg"], ["m", "dot"])) #0

# 다른사람 코드
def solution(s1, s2):
    return len(set(s1)&set(s2))
# 집합으로 비교

# 짝수는 싫어요
def solution(n):
    return list(range(1, n+1, 2))

print(solution(10)) # [1, 3, 5, 7, 9]
print(solution(15)) # [1, 3, 5, 7, 9, 11, 13, 15]

# 자릿수 더하기
def solution(n):
    answer = 0
    answer = sum(list(map(int, list(str(n)))))  #list(str(n)) 이 아니라 str(n)만해도 됨
    return answer
print(solution(1234)) # 10
print(solution(930211)) # 16

# 다른사람 코드
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer

# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter,'')

print(solution("abcdef", "f")) # "abcde"
print(solution("BCBdbe", "B")) # "Cdbe"

#피자 나눠 먹기 (1)
# 7조각 피자 
def solution(n):
    answer = 0
    a, b = divmod(n, 7)
    if b == 0:
        answer = a
    else:
        answer = a + 1
    return answer
print(solution(7)) #1
print(solution(1)) #1
print(solution(15)) #3

# 다른사람 코드  / ???
def solution(n):
    return (n - 1) // 7 + 1

# 옷가게 할인 받기
def solution(price):
    answer = 0
    sale = 1
    if price >= 500000:
        sale = 0.8
    elif price >= 300000:
        sale = 0.9
    elif price >= 100000:
        sale = 0.95
    answer = int(price * sale)
    return answer
print(solution(150000)) # 142,500
print(solution(580000)) # 464,000
print(solution(1))

# 문자 반복 출력하기
def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n
    return answer
print(solution("hello", 3)) # 	"hhheeellllllooo"

# 가위 바위 보
# 가위 2, 바위 0, 보 5
# 이기는 값 순서대로 문자열 출력
#2 > 0
#0 > 5
#5 > 2
def solution(rsp):
    answer = ''
    for i in rsp:
       if i == '2':
           answer += '0'
       elif i == '0':
           answer += '5'
       elif i == '5':
           answer += '2'
    return answer

print(solution('2')) #"0"
print(solution('205')) #"052"

# 다른사람 코드
def solution(rsp):
    d = {
        '0':'5',
        '2':'0',
        '5':'2'
        }
    return ''.join(d[i] for i in rsp)  # ★★ join 활용


# lambda 매개변수 : 표현식
# (lambda 매개변수들: 식)(인수들)
# (lambda x,y: x + y)(10, 20) # 30

# 배열 자르기
def solution(numbers, num1, num2):
    answer = []
    answer = numbers[num1 : num2 + 1]
    return answer
print(solution([1, 2, 3, 4, 5], 1, 3)) #[2, 3, 4]
print(solution([1, 3, 5], 1, 2)) #[3, 5]

# 세균 증식
# 1시간에 2배
    # 2마리 4, 8 16 32, 64 ...
    # 7마리, 14, 28 ,56, 112...
def solution(n, t):
    answer = n
    while t > 0:
        answer *= 2
        t -= 1
    return answer
print(solution(2, 10)) # 2048
print(solution(7, 15)) # 229376

# 다른사람 코드
def solution(n, t):
    answer = 2**t * n
    return answer

# 암호 해독
def solution(cipher, code):
    answer = ''
    range_a = int(len(cipher)/code) + 1
    for i in range(1, range_a):
        answer += cipher[code*i-1]
    return answer
print(solution("dfjardstddetckdaccccdegk", 4)) # "attack"
print(solution("pfqallllabwaoclk", 2)) # "fallback"

# 다른사람 코드 / ★★ 문자열 나누기
def solution(cipher, code):
    answer = cipher[code-1::code]   # code-1 인덱스부터: 끝까지 : code 단위로 띄어서
    return answer

# 모음 제거
def solution(my_string):
    my_string = my_string.replace('a','')
    my_string = my_string.replace('i','')
    my_string = my_string.replace('u','')
    my_string = my_string.replace('e','')
    my_string = my_string.replace('o','')
    return my_string
print(solution("nice to meet you")) # "nc t mt y"

# 다른 사람 코드 
def solution(my_string):
    return "".join([i for i in my_string if not(i in "aeiou")])

# 영어가 싫어요 
e_dict = {
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
}
# 선언해놓고 쓸줄 몰라서 보류

def solution(numbers):
    numbers = numbers.replace('one','1')
    numbers = numbers.replace('two','2')
    numbers = numbers.replace('three','3')
    numbers = numbers.replace('four','4')
    numbers = numbers.replace('five','5')
    numbers = numbers.replace('six','6')
    numbers = numbers.replace('seven','7')
    numbers = numbers.replace('eight','8')
    numbers = numbers.replace('nine','9')
    numbers = numbers.replace('zero','0')
    return int(numbers)
print(solution("onetwothreefourfivesixseveneightnine"))
print(solution("onefourzerosixsevenone"))

# 다른사람 코드 1
def solution(numbers):
    for num, eng in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(eng, str(num))
    return int(numbers)
# 다른사람 코드 2
def solution(numbers):
    dic = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    i=0
    for word in dic:
        numbers = numbers.replace(word, str(i))
        i+=1
    return int(numbers)