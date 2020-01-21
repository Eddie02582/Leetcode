/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode current = head;        
        while (l1 != null && l2 != null)
        {            
            if (l1.val < l2.val )
            {       
                current.next = new ListNode(l1.val); 
                l1 = l1.next;
            }
            else 
            {
               current.next = new ListNode(l2.val); 
                l2 = l2.next; 
            }          
            current = current.next;           
        }
        current.next = l1 != null ?  l1 :l2 ;
        
        return head.next;
    }
}