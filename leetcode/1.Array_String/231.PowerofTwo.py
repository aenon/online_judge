#  231. Power of Two 

#  Given an integer, write a function to determine if it is a power of two.

# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = bin(n)
        if n == 0:
            return False
        if n == 1:
            return True
        return s[3:].count('1') == 0

    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # if n is power of 2, then n - 1 is '1111...1'
        return n > 0 and (n & n - 1) == 0    

    def isPowerOfTwo3(self, n):
        """
        samee as solution 2
        :type n: int
        :rtype: bool
        """
        return n > 0 and (n & ~-n) == 0   