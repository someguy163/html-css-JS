alist = ['a1','a2','a3']
blist = ['b1','b2','b3']
for a,b in zip(alist,blist):
    print(a,b)

for i,(a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)    