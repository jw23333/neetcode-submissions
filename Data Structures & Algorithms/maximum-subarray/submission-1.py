class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        best=nums[0]
        for num in nums:
            cur=cur+num
            if cur>0:
                best=max(cur,best)
            else:
                best=max(cur,best)
                cur=0
        return best