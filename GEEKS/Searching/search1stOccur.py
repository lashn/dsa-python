A=[5,10,10,10,20,20]
x=10 # find first occ
n=len(A)
low=0
high=n-1

def binsearch(A,low,high, x):
    while(low<=high):
        mid=(low+high)//2
        if x==A[mid]:
            if mid>0 and x==A[mid-1]: #only look for mid -1 that could be my 1st occur ,doesn't matter right side
                high = mid - 1
                # binsearch(A, low, high, x) # for recursive method
            else:
                return mid
        elif x<A[mid]:
            high=mid-1
            # binsearch(A, low, high, x) # for recursive method
        elif x>A[mid]:
            low = mid + 1
            binsearch(A, low, high, x)
    return -1

print(binsearch(A,low,high,x))