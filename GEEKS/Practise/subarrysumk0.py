# A=[-3,4,-3,-1, 1]
#   #0  1  2  3  4

A=[1,2,3,4,5,0]
  #h[-3, 1,-2,-3(error as it already in hash), ....  ]
#Subarray with 0 sum

#first is to compute prefix sum and had it to hash
#when we add it, we will get to know if

#subarrays a[0 0] a[0 1] a[0 i] / a[1] a[]

n=len(A)
p=[0]*n
h=[[] for _ in range(n)]
ans=False
for i in range(n):
    if A[i]==0:
        print("true")
        ans = True
        break

    if i==0:
        p[i]=A[i]

    else:
        p[i]=p[i-1]+A[i]
    hasind=p[i]%n


    if p[i] in h[hasind]:
        print("true")
        ans=True
        break
    print(p)
    print(h)
    h[hasind].append(p[i])

if not ans:
    print("False")