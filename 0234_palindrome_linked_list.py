# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # head = self.createList()
        # print(head)
        
#         INEFFICIENT
#         newList = None
        
#         slow = fast = head
#         while fast and fast.next:
#             slow = slow.next
#             fast = fast.next.next
        
#         newListHead = None
#         oldNode = None
#         while slow:
#             newNode = ListNode(slow.val)
#             # print("newNode", newNode)
#             newNode.next = oldNode
#             newListHead = newNode
#             oldNode = newNode
#             slow = slow.next
#         # print(newListHead)
        
#         while newListHead:
#             # print(head.val, newListHead.val)
#             if head.val != newListHead.val:
#                 return False
#             head = head.next
#             newListHead = newListHead.next
#         return True



#       USING O(N) SPACE
        node_list = []
        while head:
            node_list.append(head.val)
            # node_list += head.val,
            head = head.next
        return node_list == node_list[::-1]
        
        
    def createList(self):
        head = curr = ListNode(1)
        curr.next = ListNode(2)
        curr = curr.next
        curr.next = ListNode(3)
        curr = curr.next
        curr.next = ListNode(2)
        curr = curr.next
        curr.next = ListNode(1)
        return head
            
        
