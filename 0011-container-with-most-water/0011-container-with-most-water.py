class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        L = 0
        R = n-1
        maxarea = 0
        while L<R:
            width = R-L
            heightt = min(height[L],height[R])
            currentarea = width * heightt
            maxarea = max(currentarea,maxarea)
            if height[L] < height[R]:
                L+=1
            else:
                R-=1
        return maxarea            
        