class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == []:
            return []
        result= []
        intervals.sort()
        for interval in intervals:
            if result == [] or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1],interval[1])
        return result                       
# intervals = [[1,3],[2,6],[8,10],[15,18]]
# result = [[1,3]] 
# intervals = [[2,6],[8,10],[15,18]]
# result[0][1], result[-1][1]
# result[-1][1] = 3  interval[0] = 2  as 3>2  we will merge not append
# result = [[1,3]]
# max(3,6)= 6  result[-1][1] =6







        