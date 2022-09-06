A=[1,2,4,8,9,20,40]
x= 32
'''
A[i]+A[j]+A[k]=X
for i in range n
    j in i to n
        k in j to n
            i+j+k

infer:
keep i as const and look for j,k in the right side
i=0; find j,k using 2 pointer tech
'''
#if not sorted A.sort()
n=len(A)

def twopoint(j,f,k=n-1):
    while(j<k):
        if A[j]+A[k]==f:
            return True
        elif A[j]+A[k]<f:
            j+=1
        elif A[j] + A[k] > f:
            k-=1
    return False

found3= False
k=n-1
for i in range(n-2):
    f=x-A[i]
    j = i + 1
    if twopoint(j,f):
        found3=True
        print(found3)
        break
if not found3:
    print(found3)








