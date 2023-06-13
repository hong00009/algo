# 문제
# 다음은 10명의 학생들의 혈액형(A, B, AB, O) 데이터입니다.
# ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']
# for 문을 이용하여 각 혈액형 별 학생수를 구하십시오.
# 출력
# {'A': 3, 'O': 3, 'B': 2, 'AB': 2}  / 딕셔너리

people = ['A', 'A', 'A', 'O', 'B', 'B', 'O', 'AB', 'AB', 'O']

dict_b = {'A': 0,
              'O': 0,
              'B': 0,
              'AB': 0,
              }

# 강사님의 간결한 코드
for blood in people:
    dict_b[blood] += 1
print(dict_b)

print('------')

# 내코드 / 딕셔너리 개별값 할당 방법을 잘 몰라서, key index 하나하나 지정해서 값을 넣다보니 코드가 장황해졌음
a_people = 0
b_people = 0
o_people = 0
ab_people = 0

for i in range(10):
    if people[i] == 'A':
        a_people = a_people + 1
    elif people[i] == 'B':
        b_people = b_people + 1
    elif people[i] == 'O':
        o_people = o_people + 1
    elif people[i] == 'AB':
        ab_people = ab_people + 1
    else:
        print()

dict_b['A'] = a_people
dict_b['O'] = o_people
dict_b['B'] = b_people
dict_b['AB'] = ab_people
print(dict_b)
# 출력값 {'A': 3, 'O': 3, 'B': 2, 'AB': 2}



# 다른 방법

location = ['서울', '대전', '대전', '부산']  #

# 얻고싶은 결과는 아래와 같지만, 앞으로 어떤 데이터가 추가될지 알 수 없는 상황에서는

# location_dict = {
#     '서울': 1,
#     '대전': 2,
#     '부산': 1,
# }
# 다른 지역이 추가되더라도 늘어나도록 처리 예정

# 1) 이미 지역목록에 있는 지역에서 value가 추가되는 경우
# 2) 지역 목록에 없는 지역에서 value가 추가되는 경우
location_dict ={} #비어있는 딕셔너리 표 하나 만들어둠

for l in location:
    
    # 이미 지역목록에 지역 기록을 한 경우
    if l in location_dict.keys():  #딕셔너리 안의 key에 l이 들어있는지? 
        location_dict[l] += 1
        
    # 처음으로 등장한 지역 경우
    else:
        location_dict[l] = 1
print(location_dict)
