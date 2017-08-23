# 371. Sum of Two Integers 

# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

# Example:
# Given a = 1 and b = 2, return 3. 

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        bit_length = 32
        max_int = 1 << bit_length >> 1
        mask = ~(~0 << 32)
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= max_int else ~(a ^ mask)

class Solution1(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        The cheating method: use operator.add()
        """
        import operator
        return operator.add(a, b)