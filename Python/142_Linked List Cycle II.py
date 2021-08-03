class Solution(object):
    def detectCycle(self, head):
        
        slow,fast = head ,head
        loop = False
        
        while fast and fast.next :            
            slow = slow.next            
            fast = fast.next.next            
            if slow == fast:
                break              
              
        if not fast or not  fast.next:
            return        
        
        slow2 = head
        while slow2 != slow:
            slow, slow2 = slow.next, slow2.next     
        
        return slow