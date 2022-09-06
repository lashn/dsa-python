inputString="abba"
a=inputString
n = len(a)
palindrome = True
for i in range(n):
    if i > n:
        break
    print(inputString[i],a[n-1])

    if a[i] != a[n - 1]:
        palindrome = False
        break
    n -= 1
print(palindrome)