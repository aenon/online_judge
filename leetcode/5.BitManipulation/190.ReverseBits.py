#  190. Reverse Bits 

#  Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

# Follow up:
# If this function is called many times, how would you optimize it?

# Related problem: Reverse Integer

# Companies

# Related Topics

# Similar Questions
# Number of 1 Bits

class Solution:
    # @param n, an integer
    # @return an integer
    """
    if n is negative, keep the '-' sign in the converted part
    """
    def reverseBits(self, n):
        if n < 0:
            signbit = 3
        else:
            signbit = 2
        string = bin(n)
        string = string[:signbit] + string[signbit:].zfill(32)[::-1]
        return int(string, 2)
