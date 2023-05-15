#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

# Runtime beats 7.76 % of python3 submissions
# Your memory usage beats 6.07 % of python3 submissions (16.6 MB)
# Other ideas could be first to find the shortest string in strs, then compare each character in the shortest string with the other strings in strs
# Another idea is to create a trie tree, then find the longest common prefix
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
         # if strs is empty, return empty string
        if len(strs) == 0:
            return ''
        
        # if strs has only one element, return that element
        if len(strs) == 1:
            return strs[0]
        
        # if strs has more than one element, find the longest common prefix
        prefix = []
        for ch in strs[0]:
            prefix.append(ch)
        
        # compare the prefix with each element in strs
        for str_index in range(len(strs)):
            prefix_index = 0
            if strs[str_index] == '':
                return ''
            
            # compare each character in the current string with the prefix
            for ch in strs[str_index]:
                if prefix == []:
                    return ''
                if prefix_index >= len(prefix):
                    break
                if ch != prefix[prefix_index]:
                    prefix = prefix[:prefix_index]
                    break
                prefix_index += 1
            
            # check if the current string is shorter than the current prefix
            if len(strs[str_index]) < len(prefix):
                prefix = prefix[:len(strs[str_index])]
        
        return ''.join(prefix)
     
# @lc code=end

