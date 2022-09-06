A=[6,8,-1,7] #sum=94
#print all subarrays
#[0,0],[0,1]...[1,1],[1,2],[1,3]...[2,2]....[n-1,n-1]

sum=0
count=0
tsum=0
for i in range(len(A)):
    sum = 0
    for j in range(i,len(A)):
        # print(i,j) #prints all sub arrays indexes
        # print(A[i],A[j])
        # print()
        count += 1
        sum = sum + A[j]
        tsum = tsum + sum

        # for k in range(i,j):
        #     print(A[k],end=' ') # print all the indices
        # print()


print("through iterative loop ",count)
print("through iterative loop sum ",tsum)

#formula
#[0,0],[0,1]...[1,1],[1,2],[1,3]...[2,2]....[n-1,n-1]
#this is a natural num series N,N-1,N-2,....1

N=len(A)
countnum=(N*(N+1))//2
print("through formula ",countnum)
