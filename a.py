class Solution:
    # @param A : integer
    # @return a list of integers
    def getRow(self, A):
        curr=[1]*(A+1)
        if A<2: return curr
        prev=self.getRow(A-1)
        for i in range(1,A):
            curr[i]=prev[i]+prev[i-1]
        return curr
       
