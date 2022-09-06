# A=[1,5,7,-1]; k=6
# A=[10,1,1,1] ;k=11
A=[1,1,1,1]; k=2
# A=[1,2,2,2,3]; k=4

#first soln
'''
for i in range(n):
    for j in range(n+1):
        if sum[i,j]==k:
            count+=1
O(N-2)        
'''
#2nd soln
'''
#A[i]+A[j]=k
A[j]=k-A[i]
5=6-1

O(N)
A[i] might repeat
1st would be to hash A[i]
2nd would be to check if there any A[j] in the hash => count+=1

'''
n=len(A)
d={}
for i in range(n):
    if A[i] in d:
        d[A[i]]+=1
    else:
        d[A[i]] = 1
#hash=[1:1,5:1,7:1,-1:1]
print(d)
count=0

for i in range(n):
    count+=d[k-A[i]]
    if A[i]==k-A[i]:
        count-=1
print(count/2)

''' prog to find if it exists or not
    b=k-A[i]
    if (A[i]!=b and b in d):
        return True
    if (A[i]==b and d[b]>1):
        return False
'''
# A=[1,2,2,2,3]
# k=4
# count=4 (3+1)
# A=[1,3] => i=1,3 => 2/2 =>1
# A=[2,2,2] => i=2, 3*3 => 9 - 3 i=A[i] --1 => 6/2 =>3
# (3+3+3+2)=9+2=11-3=8/2=4
# 10/2=
# count+=d[k-A[i]]






