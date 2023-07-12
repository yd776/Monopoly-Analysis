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


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def findOccurences(self, A):
        
        A.sort()
        counts=dict()
        for i in A:
            if i in counts:
                counts[i]+=1
            else:
                counts[i] =1
        my_list = list(counts.values())
        return my_list
        
        
        
