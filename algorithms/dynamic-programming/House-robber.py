class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        last, now = 0,0
        for currentRob in nums:
            last, now = now, max(last + currentRob, now)
        return max(last, now)