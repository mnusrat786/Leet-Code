class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []  
        result=[]      
        intervals.sort()
        for interval in intervals:
            if result == [] or result[-1][1] < interval [0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result
        # [[1,3],[2,6],[8,10],[15,18]]
        # result = []
                    
        
            
    