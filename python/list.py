list_a = [1,2,3]
list_b = [4,5,6]

print("list_a")
print(list_a)
print("list_b")
print(list_a)

print("list 연산자")
print("list_a + list_b = " , list_a + list_b)
print("list_a * 3 = " ,list_a * 3)

# 길이구하기
print("길이구하기")
print("list_a" , len(list_a))
cities = ['1','2','3','4','5','6','7','8']
cities[0:2]
cities[5:]
cities[-6:]


# 배열수정
# insert
color = ['red','blue','green']
color.insert(0,'orange')
print(color)

# remove
color.remove('orange')
print(color)

# del
list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")

# 제거 방법[1] – del
del list_a[1]
print("del list_a[1]:", list_a)

# 제거 방법[2] – pop()
list_a.pop(2)
print("pop(2):", list_a)



