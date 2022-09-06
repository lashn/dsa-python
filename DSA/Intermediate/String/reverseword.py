A="the sky is     blue"
ans = ""
current = ""
# " the  sky is blue"
# "blue is sky the"
n = len(A)
for i in range(len(A)):
    print(A[i])
    if A[i] != ' ':
        current += A[i]
        print(current)
    else:
        current = current[::-1]
        ans = current + ans
        if i < n:
            ans = " " + ans
print(A)