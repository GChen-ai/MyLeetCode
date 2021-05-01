class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        s1=set(nums1)
        s2=set(nums2)
        result=[]
        for n in s1:
            if n in s2:
                result.append(n)
        return result