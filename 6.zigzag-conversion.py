#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#
# Your runtime beats 5.02 % of python3 submissions
# Your memory usage beats 11.07 % of python3 submissions (16.7 MB)
# Another solution is to create a list of strings and append the characters to the list. Then join the list of strings to form the final string.
# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        # If numRows is 1, return the string
        if numRows == 1:
            return s
        
        x = 0
        y = 0   
        ph = {} # Placeholder for the coordinates
        prev_num = 0

        # Create a dictionary with the coordinates of the zigzag
        for i in range(len(s)):
            if x == 0:
                ph[(x,y)] = s[i]
                prev_num = x
                x += 1
            elif x < numRows - 1 and x > prev_num:
                ph[(x,y)] = s[i]
                prev_num = x
                x += 1
            else:
                ph[(x,y)] = s[i]
                prev_num = x
                x -= 1
                y += 1

        # Combine the string from the dictionary
        combine = ''
        for x in range(numRows):
            for y in range(len(s)):
                if (x,y) in ph:
                    combine += ph[(x,y)]

        return combine

# @lc code=end

