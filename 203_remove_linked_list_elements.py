# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            if curr.val == val:
                if prev == None: # delete first node
                    head = curr.next
                    curr = curr.next
                else:
                    curr = curr.next
                    prev.next = curr
            else:
                prev = curr
                curr = curr.next
                
        return head
        
