#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
# Your runtime beats 36.22 % of python3 submissions.
# Your memory usage beats 25.32 % of python3 submissions (16.5 MB).
# Another way to solve this problem dynamically program it which mean to breaking to down to smaller subproblems and storing the results of the subproblems
# Another way to solve this problem is to use Manacher's algorithm which is a linear time algorithm that finds all the palindromes in a string

class Solution:
    def longestPalindrome(self, s: str) -> str:

        # If the string is empty or only one character, return the string
        if s == s[::-1]: return s

        # Setting the longest palindrome to the first letter in the string
        longest_palindrome = s[0]

        # Looping through the string
        index = 0
        for ch in s:

            # Finding the index of all the same letters
            same_letter = [x for x, ltr in enumerate(s) if ltr == ch]

            # Looping through the indexes of the same letters
            for x in same_letter:

                # If the index is greater than the current index
                if x > index:

                    # If the string is a palindrome
                    if s[index:x+1] == s[index:x+1][::-1]:

                        # If the length of the string is greater than the length of the longest palindrome
                        if len(s[index:x+1]) > len(longest_palindrome):
                            longest_palindrome = s[index:x+1]

            index += 1
        
        return longest_palindrome
        
# @lc code=end

