#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
#
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# Your runtime beats 8.43 % of python3 submissions.
# Your memory usage beats 5.64 % of python3 submissions (16.4 MB).
# Other ways to solve this problem is to use recursion or to use a stack
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        l1_reverse = []
        l2_reverse = []

        # Looping through the linked list
        while l1:
            l1_reverse.append(l1.val)
            l1 = l1.next
        # Reversing the list
        l1_reverse = l1_reverse[::-1]
        l1_reverse = ''.join(A(x) for x in l1_reverse)

        while l2:
            l2_reverse.append(l2.val)
            l2 = l2.next
        l2_reverse = l2_reverse[::-1]
        l2_reverse = ''.join(str(x) for x in l2_reverse)

        # Adding the two numbers together
        result = str(int(l1_reverse) + int(l2_reverse))

        # Reversing the result
        result_arr = []
        for x in result[::-1]:
            result_arr.append(int(x))

        # Creating the linked list
        head = ListNode(result_arr[0])
        current = head
        for value in result_arr[1:]:
            current.next = ListNode(value)
            current = current.next

        return head     
        
# @lc code=end