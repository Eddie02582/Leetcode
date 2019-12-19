# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        s = "".join(map(lambda x:str(x),arr))
        return int(s,2)
        
    def getDecimalValue(self, head):
        answer = 0
        while head: 
            answer = 2*answer + head.val 
            head = head.next 
        return answer 