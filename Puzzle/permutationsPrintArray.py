class solution:
    def __init__(self):
        self.ref={}
        self.result=[]
        self.index=-1
        self.bool=[True] * len(arr)

    ''''
         0 1 2
    arr=[1,2,3]
    ref-0:1 1:1 2:1 132 2:1
    123         132 213 231 312 321
    
    '''
    def printallPerm(self,a,bool, res,temp,n):

        if n==len(temp):
            return temp
        for i in range(n):
            #i=0
            bool[i] = False
            if bool[i]:
                # 0:F,1:T,2:T
                self.printallPerm(a, bool, res, temp, n)

                temp.append[a[i]]

        bool = [True] * n
        res.append()




#     all perm and combinations
#     12345, 21345,31245,...

arr=[1,2,3]
sol=solution()
res=[]
temp=[]
n=len(temp)
bool=[True] * n
ans=sol.printallPerm(arr,bool, res,temp,n)
print(ans)



        # n = len(arr)
        # # for k in range(n):
        #
        # for i in range(n):
        #     temp = []
        #     self.ref = {}
        #     self.ref[a[i]]=1
        #     temp.append(a[i])
        #     for j in range(n):
        #         print(j)
        #         if a[j] not in self.ref:
        #             temp.append(a[j])
        #             self.ref[a[j]] = 1
        #         # print(temp)
        #         if len(temp)==n:
        #             print(temp,j)
        #             self.result.append(temp)
        #             break
        # return self.result