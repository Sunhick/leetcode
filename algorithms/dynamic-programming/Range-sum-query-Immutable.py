import math 

class NumArray(object):
    
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.dpsum = nums
        
        for i in range(1, len(nums)):
            self.dpsum[i] += self.dpsum[i-1]
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.dpsum[j] if i == 0 else self.dpsum[j] - self.dpsum[i-1]


# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)