A=[6,8,-1,7] #sum=94
#print all subarrays
#[0,0],[0,1]...[1,1],[1,2],[1,3]...[2,2]....[n-1,n-1]

sum=0
count=0
tsum=0
n=len(A)
# Prefix sum
PF=[0]*n
PF[0]=A[0]
for i in range(1,len(A)):
    PF[i]=PF[i-1]+A[i]
print("Prefix sum ",PF)

#find all sum in O(N)
#S[0],S[0 1], S[0 2]..S[1 1]
# S[1 1]=> PF[R] - PF[L-1]=> PF[j]-PF[i-1]
#PF[0]+PF[1],...S[1 1]=> PF[R-L+1]
for i in range(len(A)):
    sum=0
    for j in range(i,len(A)):
        if i==0:
            sum=sum+PF[j]
            # print(sum)
        else:
            sum=sum+PF[j]-PF[i-1]
    tsum=sum+tsum

print("through prefix sum ",tsum)

