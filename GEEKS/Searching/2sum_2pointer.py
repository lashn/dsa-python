# A=[2,4,8,9,11,12,20,30]
# x=23

A=[1,2,3,4,5,6]
x=45
'''
A=[2,4,8,9,11,12,20,30]
   i                 j
        i<j
    A[i]+A[j]==
    :return
    A[i]+A[j]<x:
        i+=1
    
    A[i]+A[j]>x:
        j-=1
end return -1
'''
i=0
n=len(A)
j=n-1
found=False
while(i<j):
    if A[i]+A[j]==x:
        found=True
        print(i,j,True)
        break
    elif A[i]+A[j]<x:
        i+=1
    elif A[i]+A[j]>x:
        j-=1
if not found:
    print(False)



