class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        counts=dict()
        for i in A:
            if i  in counts:
                return i
            else:
                counts[i]=1
            
        return -1
        
