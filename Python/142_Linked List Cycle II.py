# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        slow,fast = head ,head
        loop = False
        
        while fast and fast.next :            
            slow = slow.next            
            fast = fast.next.next            
            if slow==fast:
                break              
              
        if not fast or not  fast.next:
            return        
        
        slow2 = head
        while slow2 != slow:
            slow, slow2 = slow.next, slow2.next     
        
        return slow
     
        
sol = Solution()

l1 = ListNode(3)
l2 = ListNode(2)
l3 = ListNode(0)
l4 = ListNode(-4)

l1.next = l2
l2.next = l3 
l3.next = l4 
l4.next = l2 



sol.detectCycle(l1)