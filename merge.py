class Solution:
    
   
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return []
        sorted_intervals = intervals
        res = [sorted_intervals[0]]
        print(res)
        for i in sorted_intervals[1:]:
            print(i)
            #the next node's smallest value is smaller than the prev node's largest value, 
            if i[0] <= res[-1][1]:
                #left boundary is the largest value
                print(res[-1][1])
                res[-1][1]=max(i[1], res[-1][1])
            else:
                res.append(i)
        return res
