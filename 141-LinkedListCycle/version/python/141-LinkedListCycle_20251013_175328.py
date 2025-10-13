# Last updated: 10/13/2025, 5:53:28 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):

        visited_nodes = set()

        current_node = head
        while current_node is not None:
            if current_node in visited_nodes:
                return True #cycle detected

            visited_nodes.add(current_node)
            current_node = current_node.next
        return False


    