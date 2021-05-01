class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        dic={}
        result=0
        for i in range(len(row)):
            dic[row[i]]=i
        for i in range(0,len(row),2):
            if row[i]%2==0:
                if (row[i+1]-row[i]!=1):
                    temp=row[i+1]
                    loc=dic[row[i]+1]
                    row[dic[row[i]+1]],row[i+1]=row[i+1],row[i]+1
                    dic[row[i]+1]=i+1
                    dic[temp]=loc
                    result+=1
            else:
                if (row[i]-row[i+1]!=1):
                    temp=row[i+1]
                    loc=dic[row[i]-1]
                    row[dic[row[i]-1]],row[i+1]=row[i+1],row[i]-1
                    dic[row[i]-1]=i+1
                    dic[temp]=loc
                    result+=1
        return result
                
