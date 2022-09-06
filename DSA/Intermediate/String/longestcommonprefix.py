A = [ "abcd", "abcd", "efgh"]
n = len(A)
ans = ""
s = A[0]

for i in range(1, n):
    ns = len(s)
    e = A[i]
    ne = len(e)
    j = 0
    flag=True
    while (j < ns and j < ne and flag):
        if s[j] == e[j]:
            ans += e[j]  # abc
        # elif e[j]!=:
        else:
            flag=False
            ans = ans[0:j]
            if len(ans) == 0:
                print(0)
            break
        j+=1
    s = e
    print(ans)