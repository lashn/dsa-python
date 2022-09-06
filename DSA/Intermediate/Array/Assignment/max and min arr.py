A = list(map(int, input().split()))
N = A[0]
A.pop(0)
min = A[0];
max = A[0]
#6 1 3 4 5 10 -1 ip
for i in range(1, N):
    if (min > A[i]):
        min = A[i]

    elif (max < A[i]):
        max = A[i]
print(max, min)