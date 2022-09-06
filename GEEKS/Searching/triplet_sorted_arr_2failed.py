A=[1,2,4,8,9,20,40]
x=32
'''
A[i]+A[j]+A[k]=X
for i in range n
    j in i to n
        k in j to n
            i+j+k

infer:
move from high
skip elems > x
i,j < x
keep i as const and look for j,k
'''
#if not sorted A.sort()
n=len(A)
found=False
for i in range(n-1,-1,-1):
    if A[i] > x:
        i += 1
        break
nn=n-i
'''i=0  j=2 k1=1
i=0
j=nn-1
k- i+1 to j-1
    if A[i]+A[j]+A[k]==x:
        return 
    if A[i]+A[j]+A[k]<x:
    if A[i]+A[j]+A[k]>x:
    
# while i<j and i>2
    if A[i]+A[j]
A=[1,2,4,8,9,20]
x=32 
'''
i=0
j=nn-1
k=i+1
while (i<j):
    for k in range(i+1,j):
        if A[i] + A[j] + A[k] == x:
            found=True
            print(found)
        elif A[i] + A[j] + A[k] < x:
            i+=1
        elif A[i] + A[j] + A[k] > x:
            j-=1
if not found:
    print(found)









# while (i>0 and j>1 and k>2):
#     if A[i]>x:
#         i+=1;j+=1;k+=1
#     else:
#         #A=[1,2,4,8,9,20]
#         new=n-1-i
#         for j in range(i+1,n):
#             if A[i]=
#             # j+=i;k+=j
#         if A[i]


