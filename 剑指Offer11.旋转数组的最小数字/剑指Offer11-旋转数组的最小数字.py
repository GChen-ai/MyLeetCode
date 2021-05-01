class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        l=0
        r=len(numbers)-1
        while (l<r):
            mid=(l+r)//2
            if numbers[mid]>numbers[r]:
                l=mid+1
            elif numbers[mid]<numbers[r]:
                r=mid
            else:
                r-=1
        return numbers[l]