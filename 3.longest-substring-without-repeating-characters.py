#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
# Your runtime beats 5.68 % of python3 submissions.
# Your memory usage beats 10.98 % of python3 submissions (19.1 MB).
# The sliding window solution is the fastest
# Sliding window is when you have a window that slides through the array. Then you can keep track of the longest substring without repeating characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        # if the string is empty or has only one character
        if len(s) < 2:
            return len(s)
        
        # create a hashmap with key as the index of the character and value as the character
        hashmap = {}
        for x,y in enumerate(s):
            hashmap[x] = y

        length = []
        for x in hashmap:
            
            # if the index is the last index in the hashmap, break
            if x == len(hashmap)-1:
                break
            
            # create a dictionary with key as the character and value as the index
            y = x + 1
            index = {hashmap[x] : x}
            
            # loop through the hashmap until the character is the same as the next character
            while y <= len(hashmap)-1 and hashmap[x] != hashmap[y]:

                # if the character is not in the dictionary, add it to the dictionary
                if hashmap[y] not in index:
                    index[hashmap[y]] = y
                else:
                    break

                y += 1

            length.append(len(index))    

        return max(length)    
# @lc code=end

