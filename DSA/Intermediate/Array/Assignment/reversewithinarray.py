# A=[1,2,10,7,6,3,4]
#
# n=len(A)

# print("original A "+str(A))
# #rotate using while
# l=0;r=n-1
# while(l<r):
#     A[l], A[r] = A[r], A[l]
#     l+=1
#     r-=1
# print("while loop "+str(A))
#
# #rotate using for
# l=0;r=n-1
# for l in range(n):
#     if(l>r):
#         break
#     A[l], A[r] = A[r], A[l]
#     r-=1
# print("for loop "+str(A))


#one more trial
items=["Shortsword", "Healing Potion", "Iron Breastplate", "Kite Shield"]

i=0;n=len(items)-1
while i<n:
    #items[i],items[n-1]=items[n-1],items[i]
    temp=items[i]
    items[i]=items[n]
    items[n]=temp
    i+=1;n-=1

print(items)
