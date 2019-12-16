# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None



class Solution:

    def deleteDuplicates(self, head) :
        if not head:
            return None

        remove = ListNode(head.val)
        current = remove
        
        while head and head.next:            
            if head.next.val != current.val:
                current.next = ListNode(head.next.val)
                current = current.next   
            head =head.next        
        return remove



    def deleteDuplicates(self, head) :
        current = head

        while current and current.next:
            if current.next.val == current.val:
                current.next = current.next.next
            else:
                current = current.next
        return head


        
        
l1 = ListNode(1)
l1.next =  ListNode(1)
l1.next.next =  ListNode(2)
l1.next.next.next =  ListNode(3)
l1.next.next.next.next =  ListNode(3)

  
sol= Solution()

sol.deleteDuplicates(l1)