A="ABCABABCD"
pat="ABC"

#naive a[i:j]=pat
# a[0:1] a[0:2] a[0 n-1], a[1:2...a[1:n-1]

n=len(A)
m=len(pat)
for i in range(n-m):
    for j in range(i+1,n):
        if pat==A[i:j+1]:
            print(i)


