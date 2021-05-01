class Solution(object):
    def getLeastNumbers(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        def partion(arr,l,r):
            p=arr[r]
            i=l-1
            for j in range(l,r):
                if arr[j]<p:
                    i+=1
                    arr[i],arr[j]=arr[j],arr[i]
            arr[i+1],arr[r]=arr[r],arr[i+1]
            return i+1
        def quick_sort(arr,l,r,k):
            if l<=r:
                i=partion(arr,l,r)
                if i>k:
                    quick_sort(arr,l,i-1,k)
                elif i<k:
                    quick_sort(arr,i+1,r,k)
                else:
                    return
            return
        quick_sort(arr,0,len(arr)-1,k)
        return arr[:k]