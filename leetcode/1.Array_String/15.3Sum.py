# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#     [-1, 0, 1],
#     [-1, -1, 2]
# ]

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        Sort the list; for each unique number, find two other numbers with 
        two-pointers method.
        """
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            j, k = i + 1, len(nums) -1
            while j < k:
                sum_ijk = nums[i] + nums[j] + nums[k]
                if sum_ijk == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
                elif sum_ijk < 0:
                    j += 1
                else:
                    k -= 1
            i += 1
        return result