# Given an array of integers called nums and an integer target, return the indices of the two numbers such that they add up to target. It also says, that we can assume, that each input would have exactly one solution and that we cannot use the same element twice. Here are some examples given by the problem description:

# input: nums = [2, 7, 11, 15], target = 9
# output: [0, 1]
# explanation: nums[0] + nums[1] = 2 + 7 = 9, por lo tanto, devuelve [0, 1].

#other exercise with this array nums = [3, 2, 4] target = 6

# complexity O(n)
def target_nine(nums_nine, target):
    hashmap = {}
    for i, nums in enumerate(nums_nine):
        complement = target - nums
        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[nums] = i
    
            
def target_six(nums_six, target):
    hashmap = {}
    for i, nums in enumerate(nums_six):
        complement = target - nums 
        if complement in hashmap:
            return [hashmap[complement], i]
        
        hashmap[nums] = i

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    numss = [3, 2, 4] 
    target2 = 6
    result = target_nine(nums, target)
    result2 = target_six(numss, target2)
    print(result)
    print(result2)