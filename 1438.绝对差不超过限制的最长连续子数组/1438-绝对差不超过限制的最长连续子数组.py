class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #python3没有类似c++ set的结构   只能单调递增队列维持min_val（队首）,单调递减队列维持max_val（队首）
        n = len(nums)
        inc_que = []   #monotonic_increase_queue
        dec_que = []   #monotonic_decrease_queue
        res = 0
        L, R = 0, 0
        while R < n:
            while inc_que and  nums[inc_que[-1]] >= nums[R]:
                inc_que.pop(-1)
            inc_que.append(R)
            while dec_que and nums[dec_que[-1]] <= nums[R]:
                dec_que.pop(-1)
            dec_que.append(R)

            while inc_que and dec_que and nums[dec_que[0]] - nums[inc_que[0]] > limit:
                if L == inc_que[0]:
                    inc_que.pop(0)
                if L == dec_que[0]:
                    dec_que.pop(0)
                L += 1

            res = max(res, R - L + 1)
            R += 1

        return res

