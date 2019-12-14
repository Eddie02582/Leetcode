var addTwoNumbers = function(l1, l2) {
        var head = new ListNode(0);
        var current = head;
        var carry = 0;
        while (l1 || l2){ 
            var x =  l1 ? l1.val : 0;
            var y =  l2 ? l2.val : 0;
            var n = (carry + x + y) % 10;
            carry = parseInt((carry + x + y) / 10)        
            current.next = new ListNode(n);
            current = current.next;
            l1 =  l1 ? l1.next : l1;
            l2 = l2 ? l2.next : l2;
        }
        if (carry)
            current.next = new ListNode(1);
        
        return head.next;
};