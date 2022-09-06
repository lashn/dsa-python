A=[1,5,10,10,20,20]
x=15
n=len(A)
low=0
high=n-1

def binsearch(A,low,high, x):
    while(low<=high):
        mid=(low+high)//2
        if x==A[mid]:
            return True
        elif x<A[mid]:
            high=mid-1
            # binsearch(A, low, high, x) # for recursive method
        elif x>A[mid]:
            low = mid + 1
            # binsearch(A, low, high, x) # for recursive method
    return -1

print(binsearch(A,low,high,x))