class Solution(object):
    def maxTurbulenceSize(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        if (arr==None or len(arr)==0): return 0
        dpUp=[1]*len(arr)
        dpDown=[1]*len(arr)
        result=1
        for i in range(1,len(arr)):
            if (arr[i-1]>arr[i]):
                dpDown[i]=dpUp[i-1]+1
                dpUp[i]=1
            elif (arr[i-1]<arr[i]):
                dpUp[i]=dpDown[i-1]+1
                dpDown[i]=1
            else:
                dpDown[i]=1
                dpUp[i]=1
            result=max(result,max(dpUp[i],dpDown[i]))
        return result