# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
#       ITERATIVE
                if head == None:
            return None
        
        prev = head
        curr = head.next 
        
        while prev and curr:
            if prev.next == curr:
                prev.next = None
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev


    
        
    
    
    
    
    
    
    
    
    
    
            
        
