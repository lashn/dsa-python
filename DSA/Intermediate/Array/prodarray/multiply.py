A = [1, 2, 3, 4, 5]

n=len(A)
for i in range(n):
    print("for loop")
    for j in range(i):
        print(i,j)
    for j in range(i+1,n):
        print(i,j)

for i in range(n):
    j=0
    print("while loop")
    while(j<i):
        print(i,j)
        j+=1
    #
    j+=1
    while(j<n):
        print(i,j)
        j += 1