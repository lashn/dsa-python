A=[16, 17, 4, 3, 5, 2]

n = len(A)
print(A)
max = A[n - 1]
leadarr = []
leadarr.append(max)
for i in range(n - 2, 0, -1):
    if A[i] > max:
        leadarr.append(A[i])
        max = A[i]
print(leadarr)