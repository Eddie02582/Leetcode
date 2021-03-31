/*
 * @lc app=leetcode id=2 lang=csharp
 *
 * [2] Add Two Numbers
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */

public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head = new ListNode(0);
        ListNode current = head;
        int carry = 0;
        while (l1 != null || l2 != null){

            int val1 =  l1 == null ? 0: l1.val;
            int val2 =  l2 == null ? 0: l2.val;  
            int val = (carry + val1 + val2) %10;
            carry = (carry + val1 + val2) /10;

            current.next = new ListNode(val);         
            current = current.next;
            if (l1 != null )
                l1 = l1.next;
            
            if (l2 != null )
                l2 = l2.next;                        
        }
        if (carry > 0)
            current.next =  new ListNode(carry);        
        return head.next;
        
    }
}
// @lc code=end

