# Last updated: 4/28/2025, 9:53:23 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if k ==1 or list is  empty, no reveral needed
        if not head or k ==1:
            return head

        # helper function to count node
        def getLength(node):
            count =0
            while node:
                count+=1
                node = node.next
            return count
        
        #helper function to reverse k nodes
        def reverseK(start, k):
            prev = None
            curr = start
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, start, curr
        
        #dummy node to simplify edge cases
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy

        #process each group
        while head:
            #check if there are k nodes to reverse
            curr = head
            count = 0
            for _ in range(k):
                if not curr:
                    break
                curr = curr.next
                count +=1
            if count<k:
                break
            
            #reverse k nodes
            new_start, new_end, next_group = reverseK(head, k)

            #connect to previous group
            prev_group.next = new_start
            #conect to next group
            new_end.next = next_group

            #move to next group
            prev_group = new_end
            head = next_group

        return dummy.next
        