"""
Given an array of integers `nums`, define a function that returns the "pivot" index of the array.

The "pivot" index is where the sum of all the numbers on the left of that index is equal to the sum of all the numbers on the right of that index.

If the input array does not have a "pivot" index, then the function should return `-1`. If there are more than one "pivot" indexes, then you should return the left-most "pivot" index.

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The sum of the numbers to the left of index 3 (1 + 7 + 3 = 11) is equal to the sum of numbers to the right of index 3 (5 + 6 = 11).
Also, 3 is the first index where this occurs.

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
"""
def pivot_index(nums):
    # Your code here

    # UNDERSTAND
    # don't include the actual index in either of the sums
    # lets assume that a single number would return -1

    # PLAN
    # default return variable is -1
    # if nums is empty or size 1, return -1

    # Approach 1 - runtime O(n^2)
    # The most straight forward:
    # iterate through
    # for i in range(len(nums)):
    #     # for each index, sum up the left side and the right side and compare
    #     left_sum = sum(nums[0:1])
    #     right_sum = sum(nums[i+1])

    # Approach 2
    # left_side_sum = 0
    # iterate through the array
    #   add nums[i] to left_side_sum
    #   iterate through the array from the end and work back towards i
    #       add to right_side_sum
    # 
    # this is still O(n^2) because we were recalculating the right side sum
    # how / where do we calculate the right_side_sum?

    # Approach 3
    if len(nums) <= 1:
        return -1
    # left = 0
    left = 0
    # right = sum of the entire array
    right = sum(nums)
    # iterate through the array
    # we want the index, so use range
    for i in range(len(nums)):
        #   right side = sum of the entire array - left - nums[i]
        right -= nums[i] # subtract the value at i from right first, so that right doesn't include the value at index
        # compare, and if they are the same, return i
        if left == right:
            return i
    #   add nums[i] to the left_side_sum
        left += nums[i]

    return -1

print(pivot_index([1,7,3,6,5,6]))

    
