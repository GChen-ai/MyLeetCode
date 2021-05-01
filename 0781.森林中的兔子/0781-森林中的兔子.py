class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        if answers==None or len(answers)==0:
            return 0
        answers.sort()
        count=0
        l=0
        r=0
        while r<len(answers):
            while r<len(answers) and answers[l]==answers[r]:
                if r-l>answers[r]:
                    count+=answers[l]+1
                    l+=answers[l]+1
                r+=1
            count+=answers[l]+1
            l=r
        return count