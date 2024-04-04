a =[1,2,3,4,5]
a.append(10)
a.append(20)
a

a.pop()
a

word  = input("입력하기")
word_list = list(word)
print(word_list)

result = []
for _ in range(len(word_list)) :
    result.append(word_list.pop())

print(result)    
print(word[::-1])

#  튜플
# t1 = (1,2,3)
# t2 = ('a','b',('ab','cd'))
# print(t2[::-1])

# a = (1,2,3,4,5,6,7)
# a.index(3)
# a.count(2)

# for i in a:
#     print(i,end=' ')

# a = tuple(i for i in range(10) if i %2 == 0)    
# a


# 괄호 안쓰고 컷마로 구분해서 작성하면 tuple로 된다
# a = 3,4,5
# b = 7
# c = 'a','b','c'
# print(f'type(a) : {type(a)}')
# print(f'type(b) : {type(b)}')
# print(f'type(c) : {type(c)}')
# print(f'a : {a}')
# print(f'b : {b}')
# print(f'c : {c}')

# 리턴값이 2개이상이면 튜플로 반환된다
# def get_info(num,name,phone):
#     return num , name , phone
# a = '1'
# b = 'kim'
# c = 'apple'

# result1 = get_info(a,b,c)
# print(f'type(result1) = {type(result1)}')
# print(f'result1 = {result1}')

# 언패킹
# d ,e ,f =get_info(a,b,c)
# print(d)
# print(e)
# print(f)

# 중첩튜플
# t1 = (1,2,(3,4))

# print("튜플 중첩 반복문")
# for v in t1:
#     print(v)

# 딕셔너리 튜플로 타입 변환
c1 = {'name':'blockmask','phone':'010-1234-1234','phonetype':'galaxy'}
c2 = tuple(c1)
c3 = tuple(c1.values())
print(f'tuple(딕셔너리) = {c2}')
print(f'tuple(딕셔너리.values) = {c3}')
