strings=["hello", "world","friend"]

newstr=""
n=len(strings)
for i in range(n):
    newstr += strings[i]
    if i!=n-1:
        newstr += ','
print(newstr)

# using join
# newstr=",".join(strings)

'''
    for s in strings:
        joined += s + ","
    if len(joined) != 0:
        joined = joined[:-1]
'''

