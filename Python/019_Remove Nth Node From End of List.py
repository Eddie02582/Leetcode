'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''



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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = head
        length  = 0
        while temp:
            length += 1
            temp = temp.next  
        
        remove_index ,index = length - n ,0       
        current = head
        
        if remove_index == 0:
            return head.next
            
        while current:
            index += 1
            if index == remove_index:
                current.next = current.next.next
            current = current.next
                
        return head     

    def removeNthFromEnd_simply(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head 
        while first:
            length += 1
            first = first.next

        length -= n

        first = dummy
        while length:
            length -= 1
            first = first.next
            
        first.next = first.next.next
        return dummy.next  
            


        
l1 = ListNode(1)
l1.next =  ListNode(2)
l1.next.next =  ListNode(3)  
l1.next.next.next =  ListNode(4)  
l1.next.next.next.next =  ListNode(5)        
        
        
sol = Solution()
sol.removeNthFromEnd(l1,2)        
        
l2 = ListNode(1)   
sol.removeNthFromEnd(l2,1)        
        
        
        
        
        
        
        

