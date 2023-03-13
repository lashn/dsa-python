import itertools

a = [1, 2, 3, 4, 5]
0, 1, 2 | 0, 1, 3
n = 3
# op=

# [[1],[2],[3],[4],[5]]
# [[1,2],[1,3],[1,5],[4,5],[2,5],[3,1]]

# ans=itertools.combinations(a, n)
# for i in ans:
#     print(i)

for i in range(len(a)):
    for j in range(len(a)):
        if i != j:
            for k in range(len(a)):
                # 0 1 2 3 4
                arr = [1, 2, 3]

                # i=0,j=i+1
                # 1,2; 1,3;
                # swap(arr[i],arr[j])
                # 2,1; 2,3; 3,1; 3,2
                arr1 = [1, 2, 3, 4]
                i = 0;
                j = i + 1 < n
                i = 1;
                j = 2
            1, 2, 3;            1, 2, 4;            1, 3, 4
            2, 1, 3;            2, 3, 4;            2, 1, 4

        1, 2, 3, 4
        1 - 2 - 3
        -4
    -3
    -2
    -4
-4

