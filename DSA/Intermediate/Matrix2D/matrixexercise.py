mat=[[]]
n = mat.length
m = mat[0].length
#if its square n=m=n => time comp o(n2) as its n*n matrix

# rowwise
sum=0
for i in range(n):
    sum = 0
    for j in range(m):
        sum += mat[i][j]
    print(sum)

# colwise
sum=0
for j in range(m):
    sum = 0
    for i in range(n):
        sum += mat[i][j]
    print(sum)



