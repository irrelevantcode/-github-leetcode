#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:

        index = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500,'M':1000}

        total_array = []

        # convert roman numerals to integers
        for x in range(len(s)): 
            total_array.append(index[s[x]])
            # if the current number is greater than the previous number, subtract the previous number from the current number
            if x > 0:
                if index[s[x]] > index[s[x-1]]:
                    total_array[x] = index[s[x]] - index[s[x-1]] 
                    total_array[x-1] = 0 

        # add all the numbers in the array
        total = 0
        for x in total_array:
            total += x     
        
        return total
        
# @lc code=end

