a = "hello"
b = ["hello","python"]
id(a)
id(b)

a="python2"
id(a)

def f(i,mylist):
    i = i+1
    mylist.append(0)
    print(i,mylist)

k=10
m=[1,2,3]

f(k,m)
print(k,m)