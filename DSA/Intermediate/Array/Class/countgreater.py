# Given N array elems, cout no of elem having greater atleast 1 greater elem

A=[-3,-2,6,8,4,8,5,8,10,10]

#find the max value by iter and keep a max value
#find how many max

max=A[0]
c=0
for i in range(1,len(A)):
    if max<A[i]:
        max=A[i]
        c=0
    if max==A[i]:
        c+=1

print(c)




