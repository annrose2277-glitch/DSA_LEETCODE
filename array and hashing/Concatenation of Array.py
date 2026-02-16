class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        n = len(nums)
        for i in range(2):
            for a in nums:
                ans.append(a)
        return ans  