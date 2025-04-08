# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input:

# An integer array nums of size n where n ≥ 1.
# Output:

# An integer representing the maximum sum of a contiguous subarray.

# example 1
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum = 6.

# example 2
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum = 1.


# example 3
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum = 23.

# Constraints:

# 1 ≤ nums.length ≤ 10^5
# -10^4 ≤ nums[i] ≤ 10^4

def maximum_subarray(nums):
    current_sum = nums[0]
    max_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum
            
        

            
        
               
        
        
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]  
    result = maximum_subarray(nums)
    print(result)