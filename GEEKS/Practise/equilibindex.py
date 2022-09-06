A=[1,3,5,2,2]

n = len(A)
# i=0
for i in range(1, n - 1):
    lsum = 0;
    rsum = 0
    for k in range(0, i - 1):
        lsum = lsum + A[k]
    for k in range(i + 1, n):
        rsum = rsum + A[k]
