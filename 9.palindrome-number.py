#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0: return False # If the number is negative, it can't be a palindrome

        # Reverse the number
        num = x
        reverse_num = 0
        while num != 0:
            digit = num % 10 # Get the last digit
            reverse_num = reverse_num * 10 + digit # Add the digit to the reverse number
            num //= 10 # Remove the last digit from the number

        # Check if the number is a palindrome
        if x == reverse_num:
            return True
        else:
            return False
        
# @lc code=end

