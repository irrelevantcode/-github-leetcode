#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# Your runtime beats 42.91 % of python3 submissions
# Your memory usage beats 9.66 % of python3 submissions (16.6 MB)
# Another way to solve this problem is to use the heapq module. Heaph is a binary tree that is sorted from smallest to largest which will lower the memory usage.
# Another way to solve this problem is to use the bisect module. Bisect is a binary search algorithm that will lower the runtime. Bisect will find the index of where the number should be inserted into the list keeping the list sorted.
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # combine the two lists, sort the list, then find the median of the list
        num_list = nums1 + nums2
        num_list.sort()
        median = len(num_list) // 2
        
        # if the length of the list is even, return the average of the two middle numbers
        if len(num_list) % 2 == 0:
            return (num_list[median] + num_list[median - 1]) / 2
        
        # if the length of the list is odd, return the middle number
        else:
            return num_list[median]
        
# @lc code=end

