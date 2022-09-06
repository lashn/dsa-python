

# count occurences in sorted array, using binary search

a = [10, 15, 15, 15, 15, 15, 20, 40, 40, 40, 50, 50]


def countind(a, x):
    l = len(a)
    high = l - 1
    low = 0

    while (low <= high):
        mid = (low + high) // 2
        if x > a[mid]:
            low = mid + 1
        if x < a[mid]:
            high = mid - 1
        else:
            return mid

    return -1


def binaryse(a, x):
    l = len(a)

    occur = countind(a, x)
    print("index from bin search" + str(occur))
    if occur == -1:
        return False
    count = 1
    left = occur
    right = occur
    while (left >= 0):
        if x == a[left - 1]:
            count = count + 1
            left -= 1
        else:
            break
    while (right <= l - 1):
        if x == a[right + 1]:
            count = count + 1
            right += 1
        else:
            break
    return count


x = int(input("enter a num"))
print(binaryse(a, x))

