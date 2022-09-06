# A=[1,2,3,4,5,0]
# A=[2, -5, 3, 6]
A=[2,2,1,-3,4,3,1,-2,-3,2]
  #h[-3, 1,-2,-3(error as it already in hash), ....  ]
#Subarray with 0 sum

#first is to compute prefix sum and had it to hash
#when we add it, we will get to know if

#subarrays a[0 0] a[0 1] a[0 i] / a[1] a[]

n=len(A)
p=[0]*n

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
    if p[i]==0:
        print("true")
        ans = True
        break

print(p)


if not ans:
    d = {}
    for i in range(n):
        if p[i] in d:
            d[p[i]]+=1
        else:
            d[p[i]] = 1

    print(d)
    if len(d)<len(p):
        print("true")
    else:
        print("false")



