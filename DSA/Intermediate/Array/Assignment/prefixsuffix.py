
A=[1,2,3,4,5]
B=2
n = len(A)
# create a prefix
pref = [0] * (n)
print(A)
pref[0] = A[0]

for i in range(1, len(A)):
    pref[i] = A[i] + pref[i - 1]
print(pref)

# create a suffix  array from reverse

suf = [0] * (n)
suf[n - 1] = A[n - 1]
# use decrement as suffix is reverse counter starting n-2 ... if n=10 last index is 9 in arr so using 8 (n-2)
for i in range(n - 2, -1, -1):
    suf[i] = suf[i + 1] + A[i]
print(suf)
ans=-10^9
for i in range(B):
    curr = pref[i]+suf[n-1-i]
    ans=max[ans, curr]
print(max)



