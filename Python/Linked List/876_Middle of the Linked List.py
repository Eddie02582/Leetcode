class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        count = 0
        while current.next:            
            count += 1
            current = current.next 
        
        mid =  (count + 1)//2
        
        while mid:           
            mid -= 1
            head = head.next 
        
        return head
        
    def middleNode_step(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def middleNode_array(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) / 2]



sol = Solution()       
        
l1 = ListNode(1)
l1.next =  ListNode(2)
l1.next.next =  ListNode(3)
l1.next.next.next =  ListNode(4)
l1.next.next.next.next =  ListNode(5)

assert sol.middleNode(l1) == l1.next.next 

l2 = ListNode(1)
l2.next =  ListNode(2)
l2.next.next =  ListNode(3)
l2.next.next.next =  ListNode(4)
l2.next.next.next.next =  ListNode(5)
l2.next.next.next.next.next =  ListNode(6)

assert sol.middleNode(l2) == l2.next.next.next 












