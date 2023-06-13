# 채점완료
a = input()


#  c(ASCII: 99) => C(ASCII: 67)
if a.isupper():
    ascii1 = ord(a)
    lower1 = a.lower()
    ascii2 = ord(lower1)

    print(f'{a}(ASCII: {ascii1}) => {lower1}(ASCII: {ascii2})')

elif a.islower():
    ascii1 = ord(a)
    upper1 = a.upper()
    ascii2 = ord(upper1)

    print(f'{a}(ASCII: {ascii1}) => {upper1}(ASCII: {ascii2})')
else:
    print(a)