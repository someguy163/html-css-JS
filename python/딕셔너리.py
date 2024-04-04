# 선언
# student_info = {1:'a',2:'b',3:'c',4:'d'}
# 키값호출
# student_info[1]
# 재할당
# student_info[1] = 'aaa'
# student_info
# 지우기
# del student_info[1]


# person = [('김기수',30),('홍대길',40),('강찬수',20)]
# mydict = dict(person)
# age = mydict["홍대길"]
# print(age)

# country_code = {}
# country_code = {"america":1 , "koera":2 , "japan":3}
# country_code
# country_code.keys()
# country_code["german"] = 49
# country_code.values()
# 모두출력
# country_code.items()
# key value 모두 지우기
# country_code.clear()

# a = {'name':'pay','phone':'010-1234-1234','birth':'1118'}
# a.get('name')

# for k,v in country_code.items():
#     print("key:",k)
#     print("value:",v)

# "koera" in country_code.keys()
# 2 in country_code.values()

# from collections import deque

# deque_list = deque()
# for i in range(5):
#     deque_list.append(i)

# print(deque_list)    

# deque_list.pop()
# deque_list

# deque_list = deque()
# for i in range(5):
#     deque_list.appendleft(i)
# print(deque_list)        

text = """A press release is the quickest and easiest way to get free publicity. 
If well written a press release can result in multiple published articles about your firm and tis products 
and that can mean new prospects contrackting you asking you to sell to them.""".lower().split()

from collections import defaultdict

word_count = defaultdict(lambda :0)
for word in text:
    word_count[word] +=1

from collections import OrderedDict
for i ,v in OrderedDict(sorted(word_count.items(),key=lambda t :t[1],reverse=True)).items():print(i,v)

