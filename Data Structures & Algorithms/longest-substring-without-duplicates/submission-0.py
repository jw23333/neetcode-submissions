class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen={}
        left=0
        result=0
        for index,right in enumerate(s):
            if right in seen and seen[right]>=left:
                left=seen[right]+1
            result=max(result,index-left+1)
            seen[right]=index
        return result