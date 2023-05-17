#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
# Your runtime beats 59.76 % of python3 submissions
# Your memory usage beats 5.7 % of python3 submissions (17.7 MB)
# Other ideas could be to sort the list, then use two pointers to find the two numbers
# Another idea is to use a hash table to store the numbers and their indices, then check if the target - nums[index] is in the hash table

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        check_nums = {}

        # check if the target - nums[index] is in check_nums
        for index in range(len(nums)):

            # if target - nums[index] is in check_nums, return the indices
            if target - nums[index] in check_nums:
                return [check_nums[target - nums[index]], index]
            
            # if target - nums[index] is not in check_nums, add nums[index] to check_nums
            check_nums[nums[index]] = index


        

# @lc code=end

