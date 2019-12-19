# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        if not head.next.next:
            return head
        pre = head
        cur = head.next
        while cur and cur.next:
            tmp = cur.next
            cur.next = cur.next.next
            cur = cur.next
            tmp.next = pre.next
            pre.next = tmp
            pre = pre.next
        return head
        
 
datas = [1,2,3,4,5]
head = ListNode(0)
current = head
for data in datas:
    head.next = ListNode(data)
    head = head.next
    
sol = Solution()
sol.oddEvenList(current.next)