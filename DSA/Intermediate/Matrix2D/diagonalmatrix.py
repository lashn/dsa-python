#diagonal prints (0,0),(1,1)(2,2)
mat=[[]]
n = mat.length
m = mat[0].length

for i in range(n):
    sum = 0
    for j in range(m):
        sum += mat[i][j]
    print(sum)

#diagonal print all