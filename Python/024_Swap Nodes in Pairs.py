# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


# 0->1->2->3->4->5
# 0->2->1->3->4->5
#change 4->3
# node1->_next
# node2->node1
# prev ->node1

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode(0,head)
        current = node.next
        prev = node
        while current and current.next:
            node1 = current
            node2 = current.next
            _next = node2.next
            
            node1.next = _next            
            node2.next = node1            
            prev.next  = node2               
            prev = node1  
            current = prev.next   
        return node.next        
 
     
node = ListNode(1)    
node.next =  ListNode(2)
node.next.next =  ListNode(3)  
node.next.next.next =  ListNode(4)      

sol = Solution()
sol.swapPairs(node)    