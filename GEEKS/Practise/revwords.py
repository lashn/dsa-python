S="iam.like.this.program.very.much"
'''not working
# def revstr(S, s, e):
#     revS = ""
#     for i in range(s, e + 1):
#         revS = S[i]+revS
#     return revS
#
#
# s = 0
# e = 0
# n = len(S)
# revS = revstr(S, 0, n - 1)
# print(revS)
#
# ans=""
# for i in range(n):
#     # find dots - if dot exists - then get the s and e values
#
#     if revS[i] == '.':
#         e = i - 1
#         ans=ans+revstr(revS, s, e)
#         s = i + 1
#     elif i == n - 1:
#         e = n - 1
#         ans=ans+revstr(revS, s, e)
# print(s)
'''

# internal func python
# strs = S.split(".")
# newstr = [] * len(strs)
# # i like this
# # like i
# for str in strs:
#     newstr.insert(0,str)
#
# ans = " ".join(newstr)
# print(ans)

#convert string to array


def rev(A, s, e):
    while (s < e):
        A[s], A[e] = A[e], A[s]
        s+=1
        e-=1
    return A


s = 0
e = 0
n = len(S)
A = list(S)
A = rev(A, 0, n - 1)
print(A)

for i in range(n):
    # find dots - if dot exists - then get the s and e values
    if A[i] == '.':
        e = i - 1
        rev(A, s, e)
        s = i + 1
    elif i == n - 1:
        e = n - 1
        rev(A, s, e)
    e += 1
print(A)
ans="".join(A)
print(ans)
