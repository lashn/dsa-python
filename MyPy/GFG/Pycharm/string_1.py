# check for palindrome
a = "abccba"

l = len(a)
j = l - 1

for i in range(l):
    if i != j or i == l / 2:
        if a[i] == a[j]:
            j = j - 1
        else:
            print("not palindrome")
            break

    else:
        print("its a palindrome")
        break
