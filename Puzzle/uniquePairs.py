# unique pairs
def print2pairs(arr):
    n = len(arr)
    i = 0
    while (i < n):
        j = i + 1
        while (j < n):
            print([arr[i], arr[j]])
            j += 1
        i += 1
arr=[1,2,3,4,5]
print2pairs(arr)