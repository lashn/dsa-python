A="scaler"
print(A)

#reverse ind words "cba dcb fe
# remeber string is immutable so swap is useless - will give error
# https://realpython.com/reverse-string-python/
'''
n=len(A)
i=0
rev=""
while(i<n):
    rev=rev+A[n-1]
    n-=1
print(rev)
'''

#2nd
'''
def solve(self, A):
    n = len(A)
    revA = ""
    # A="test"
    # tset
    for i in range(n):
        revA = A[i] + revA
    return revA
'''

# 3rd
n=len(A)
rev=""
rev="".join(reversed(A))
print(rev)

#4th using direct string iter
# rev=""
# #a= sample rev= as
# for s in A:
#     rev= s+rev
# print(rev)

#5th
n = len(A)
ans = ""
for i in range(n - 1, -1, -1):
    ans += A[i]
print(ans)