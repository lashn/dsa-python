A=[1,2,3,4,5,6,7]

#a[0] = a[n-1]
# 1 n-2
# 2 n-3
# i n-i-1


# brute force
n=len(A)
for i in range(n):
    if i>=n:
        break
    A[i],A[n-1] = A[n-1], A[i]
    # temp=A[i]
    # A[i]=A[n-1]
    # A[n-1]=temp
    n-=1

print(A)

# 0 5
# 1 4
# 2 3
# 3 - odd
# i n-1
# stop
# O(N/2)
# O(1)
#

