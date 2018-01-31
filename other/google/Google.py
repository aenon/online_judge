
# coding: utf-8

# ## 3sumsmaller

# In[ ]:


# // Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

# // For example, given nums = [-2, 0, 1, 3], and target = 2.

# // Return 2. Because there are two triplets which sums are less than 2:

# // [-2, 0, 1]
# // [-2, 0, 3]

# // Follow up:
#   // Could you solve it in O(n2) runtime?


# In[ ]:


# two pointer problem
# the three numbers are indexed i, left and right.


# In[10]:


nums = [-2, 1, 0, 3]
target = 2


# In[12]:


nums.sort()


# In[17]:


count = 0
for i in xrange(len(nums) - 2):
    left, right = i + 1, len(nums) - 1
    while left < right: 
        if nums[i] + nums[left] + nums[right] < target:
            count += right - left
            left += 1
        else:
            right -= 1
print(count)


# ## Android Unlock Patterns

# In[ ]:


# // Given an Android 3x3 key lock screen and two integers m and n, where 1 ≤ m ≤ n ≤ 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.

# // Rules for a valid pattern:
#   // Each pattern must connect at least m keys and at most n keys.
#   // All the keys must be distinct.
#   // If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
#   // The order of keys used matters.

# // Explanation:
# // | 1 | 2 | 3 |
# // | 4 | 5 | 6 |
# // | 7 | 8 | 9 |
# // Invalid move: 4 - 1 - 3 - 6 
# // Line 1 - 3 passes through key 2 which had not been selected in the pattern.

# // Invalid move: 4 - 1 - 9 - 2
# // Line 1 - 9 passes through key 5 which had not been selected in the pattern.

# // Valid move: 2 - 4 - 1 - 3 - 6
# // Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern

# // Valid move: 6 - 5 - 4 - 1 - 9 - 2
# // Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.

# // Example:
# // Given m = 1, n = 1, return 9.


# In[ ]:


## DFS 


# In[29]:


m, n = 2, 3


# In[20]:


def skip(a, b):
    if a == b:
        return 0
    if a + b == 10:
        return 5
    if {a, b} <= {1, 3, 7, 9}:
        return 2
    return 0


# In[25]:


visited = [0 for x in range(10)]


# In[40]:


def DFS(visited, current, remaining):
    if remaining <= 0:
        return remaining + 1
    visited[current] = 1
    total_number = 0
    for i in range(1, 10):
        to_skip = skip(current, i)
        if (not visited[i])and (to_skip == 0 or visited(to_skip)):
            total_number += DFS(visited, i, remaining - 1)
    visited[current] = 0
    return total_number


# In[37]:


total_number = 0


# In[39]:


for i in range(m, n+1):
    total_number += DFS(visited, 1, i - 1) * 4 + DFS(visited, 2, i - 1) * 4 + DFS(visited, 5, i - 1) 

