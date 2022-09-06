A=[1, 2, 3, 4, 5]
n = len(A)
p = [0] * n
p[0] = A[0]
for i in range(1, n):
    p[i] = p[i - 1] * A[i]
s = [0] * n
s[n - 1] = A[n - 1]
for i in range(n - 2, -1, -1):
    s[i] = s[i + 1] * A[i]
print(p, s)
print(s[1])
# i =0 all the suffix i+1
# i=n-1 all the prefix i-1
# i prefix[i-1]*suffix[i+1]
ans = [0] * n
for i in range(n):
    if i == 0:
        ans[0] = s[1]
    elif i == n - 1:
        ans[i] = p[i - 1]
    else:
        ans[i] = p[i - 1] * s[i + 1]
print(ans)