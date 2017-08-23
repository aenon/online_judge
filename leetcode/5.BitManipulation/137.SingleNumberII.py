#  137. Single Number II 
#   Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? 


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # not a bit manipulation answer 

        return (3*sum(set(nums)) - sum(nums)) / 2

class Solution2(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        for every bit, "one" counts if it appears 3 * k + 1 times, and "two" counts if it appears 3 * k + 2 times.
        for every number that appears 3 times, every bit of it will appear 3 times, so the corresponding bit
        in "one" and "two" are both 0.

        for each bit b in the current number, if b is 0, then "one" and "two" do not change.
        if b is not 0, then rotate among these states of (one, two): (0, 0) --> (1, 0) --> (0, 1) --> (0, 0)
        """
        one, two = 0, 0
        for number in nums:
            one, two = (~number & one) | (number & ~one & ~two), (~number & two) | (number & one)
        return one
