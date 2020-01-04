class Solution(object):
    def deleteDuplicates_(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        current = head
        numbers  = {}
        disable = set()
        while current:
            if current.val not in numbers:                
                numbers [current.val] = 1
            else:
                numbers [current.val] += 1
            current = current.next
            
        array = [ key for key in numbers.keys() if numbers[key] == 1]
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current and current.next:
            if current.next.val not in array:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy.next
        
        
    def deleteDuplicates(self, head):
        if not head:
            return None
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        while current.next and current.next.next:
            if current.next.val == current.next.next.val:
                val_prev = current.next.val
                while current.next and current.next.val == val_prev:
                    current.next = current.next.next
            else:
                current = current.next
        return dummy.next        
            
        
        
        
        
        
        
        
        
        
        
        
        