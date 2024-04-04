# 문자열 결합
colors = ['red','blue','green','yellow']
result = ''.join(colors)
print(result)

result = ' - '.join(colors)
print(result)

# 리스트 컴프리헨션
result = []
for i in range(10) :
    result.append(i)
print(result)    

[2*x for x in range(1,10+1)]

result = [i for i in range(10) if i % 2==0]
print(result)

result = [i if i % 2==0 else 10 for i in range(10)]
print(result)

word_1 = "Hello"
word_2 = "world"
result = [i + j for i in word_1 for j in word_2]
print(result)

[(x,y) for x in ['쌈밥','치킨','피자'] for y in ['사과','아이스크림','커피']]
[(x,y,z) for x in ['쌈밥','치킨','피자'] for y in ['사과','아이스크림','커피'] for z in ['배달시키기','가서 먹기']]

words = 'The quick brown fox jumps over the lazy dog'.split()
print(words)

stuff = [[w.upper(),w.lower(),len(w)]for w in words]
print(stuff)

case_1 =["A","B","C"]
case_2 = ["D","E","F"]
result = [[i + j for i in case_1] for j in case_2]
print(result)