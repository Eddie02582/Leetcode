/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode current = head;
            
        int carry = 0;
        while (l1 != null || l2 != null){
            int x =   l1 == null ? 0 :l1.val;
            int y =   l2 == null ? 0 :l2.val;
            int val = (x + y + carry)%10;
            current.next = new ListNode(val);
            carry = (x + y + carry)/10;
            
            l1 =  l1 != null ? l1.next : l1;
            l2 =  l2 != null? l2.next : l2;
            
            current = current.next;
            
        }
        if (carry > 0 ){            
           current.next =new  ListNode(carry);
        }  
        
        return head.next;
    }
}