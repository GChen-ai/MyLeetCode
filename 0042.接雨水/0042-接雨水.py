class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        N=len(height)
        left=[0]*N
        right=[0]*N
        result=0
        for i in range(1,N):
            left[i]=max(left[i-1],height[i-1])
        for i in range(N-2,-1,-1):
            right[i]=max(right[i+1],height[i+1])
        for i in range(1,N-1):
            h=min(left[i],right[i])
            if height[i]<h:
                result+=h-height[i]
        return result