# 462. Minimum Moves to Equal Array Elements II

# Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

# You may assume the array's length is at most 10,000.

# Example:

# Input:
# [1,2,3]

# Output:
# 2

# Explanation:
# Only two moves are needed (remember each move increments or decrements one element):

# [1,2,3]  =>  [2,2,3]  =>  [2,2,2]

class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #wmd_val = sorted(nums)[len(nums)/2]
        from numpy import median
        md_val = median(nums)
        #return sum(map(lambda x: abs(x - md_val), nums))
        return sum(abs(num - md_val) for num in nums)

class Solution2(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        solution from kamyu
        
        """
        def kthElement(nums, k):
            def PartitionAroundPivot(left, right, pivot_idx, nums):
                pivot_value = nums[pivot_idx]
                new_pivot_idx = left
                nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
                for i in xrange(left, right):
                    if nums[i] > pivot_value:
                        nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
                        new_pivot_idx += 1
                    
                nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
                return new_pivot_idx

            left, right = 0, len(nums) - 1
            while left <= right:
                pivot_idx = randint(left, right)
                new_pivot_idx = PartitionAroundPivot(left, right, pivot_idx, nums)
                if new_pivot_idx == k - 1:
                    return nums[new_pivot_idx]
                elif new_pivot_idx > k - 1:
                    right = new_pivot_idx - 1
                else:  # new_pivot_idx < k - 1.
                    left = new_pivot_idx + 1

        median = kthElement(nums, len(nums)/2 + 1)
        return sum(abs(num - median) for num in nums)