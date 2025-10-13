# Last updated: 10/13/2025, 6:09:20 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):

        vals = []

        current_node = head

        while current_node:
            vals.append(current_node.val)
            current_node = current_node.next
        
        return vals == vals[::-1]