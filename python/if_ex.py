# a = input("1번째 숫자 : ")
# b = input("2번째 숫자 : ")

# print()

# if a > b : 
#     print("처음 입력한 " , a ,"가 " , b , "보다 더 크다")
    
# if a < b : 
#     print("처음 입력한 " , b ,"가 " , a , "보다 더 크다")    



# print("Tell me your age")

# age = int(input())

# if age < 30 :
#     print("welcome")
# else :
#     print("nono")


# print("if 조건문에 빈 문자열 넣기")
# if "" :
#     print("빈문자열은 TRUE")
# else : 
#     print("빈문자열은 FALSE")

# score = int(input("점수 입력하세요"))

# if score > 90 : grade = 'A'
# elif score > 80 : grade = 'b'
# elif score > 70 : grade ='C'
# elif score > 60 : grade ='D'
# print(grade)

# if score > 90 : print("A")
# elif score > 80 : print("B")
# elif score > 70 : print("C")
# elif score > 60 : print("D")


print("당신이 태어난 연도를 입력하세요")
birth_year = input()
age = 2024 - int(birth_year)

if age <= 26 and age >= 20: 
    print("대학생")
elif age < 20 and age >=17:
    print("고딩")
elif age < 17 and age >=14:
    print("중딩")
elif age < 14 and age >=8:
    print("초딩")
else :
    print("학생이아닙니다")