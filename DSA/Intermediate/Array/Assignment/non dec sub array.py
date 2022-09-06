A=[1,2,3,7,6,3,4]
B=[[2,4]]

resarr = []
for i in range(len(B)):
    print(B)
    Q = B[i]
    l = Q[0]
    r = Q[1]
    # If the subarray from l to r is non decreasing, the output should be 1 else output should be 0.
    # get subarray through
    nondec = True
    for i in range(l, r):
        if A[i+1] < A[i]:
            resarr.append(0)
            nondec = False
            break

    if nondec:
        resarr.append(1)

print(resarr)

