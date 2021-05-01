class Solution(object):
    def smallestK(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        def partition(arr,l,r):
            i=l-1
            p=arr[r]
            for j in range(l,r+1):
                if arr[j]<p:
                    i+=1
                    arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[r]=arr[r],arr[i+1]
            return i+1
        
        def quicksort(arr,k,l,r):
            i=partition(arr,l,r)
            if i==k:
                return
            elif i<k:
                quicksort(arr,k,i+1,r)
            else:
                quicksort(arr,k,l,i-1)
        if arr==None or len(arr)==0 or k==0:
            return []
        quicksort(arr,k,0,len(arr)-1)
        return arr[:k]