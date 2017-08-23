# 342. Power of Four 
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example:
# Given num = 16, return true. Given num = 5, return false.

# Follow up: Could you solve it without loops/recursion? 

# O(1) / O(1)
# No recursion or loops, but using count()
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        The bin() method: count if bin(num) has one 1 and even 0's.
        """
        binstr = bin(num)[2:]
        return num > 0 and (binstr.count('1') == 1 and binstr.count('0') % 2 == 0)

# following solutions from kamyu104/leetcode

class Solution1(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        Test if num contains only one 1 and it's in an even digit.
        """
        return num > 0 and (num & (num - 1)) == 0 and ((num & 0b01010101010101010101010101010101) == num)


# O(1) / O(1)
class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        Remove all the tailing 0's, two at a time, and see if there is only one 1 left.         
        """
        while num and not (num & 0b11):
            num >>= 2
        return (num == 1)