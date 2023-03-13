d={}

d['a']=1
d['b']=2
d['c']=None
d['d']=""

for i in d:
    if d[i] not in (None,""):
        print(d[i])

