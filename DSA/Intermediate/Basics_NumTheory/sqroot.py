from math import ceil

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        #N=A pow 2
        for i in range(ceil(A/2)+1):
            if i*i==A:
                return i
        return -1

ans=Solution()
print(ans.solve(4))