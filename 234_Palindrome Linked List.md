# Palindrome Linked List

## 原題目:
```
Given the head of a singly linked list, return true if it is a palindrome.
Example 1:
   
    Input: head = [1,2,2,1]
    Output: true
   
Example 2:
    Input: head = [1,2]
    Output: false
   
Example 3:
    Input: root = [2,1], p = 2, q = 1
    Output: 2
 
Constraints:
    The number of nodes in the list is in the range [1, 105].
    0 <= Node.val <= 9
```

## 快慢指針
利用快慢指針,將慢指針儲存,當快指針結束時,表示慢指針到中間點,慢指針繼續往下並倒敘比對值

這邊有2種情況奇數和偶數
[1,2,2,1]<br>
```
    1   2  2  1
0.  f/s
1.      s  f 
2.         s    f
```
[1,2,1]<br>
```
    1   2  1
0.  f/s
1.      s  f        
```

當是奇數時slow 指針必須先下走才能判斷

#### C++
``` c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> values ;
        ListNode *fast = head;
        ListNode *slow = head; 
        
        while (fast && fast->next){            
            values.push_back(slow->val);
            fast = fast->next->next;
            slow = slow->next;
        }
        
        if(fast)           
            slow = slow->next;            
      
        
        while (slow != NULL){     
            if(slow->val != values.back())
               return false;
            values.pop_back();
            slow = slow->next;
        }
        return true;
    }
};

``` 

#### python
這邊把後半段存起來,重新從頭出發直到stack==0,所以奇數中間兩邊都會比較到

``` /usr/bin/svnadmin hotcopy /var/svn/hotcopy/DRV_AP271 /var/svn/repos/DRV_AP271
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        p = slow = fast = head
        stack = []
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        while slow:
            stack.append(slow)
            slow = slow.next
        while stack:
            if stack.pop().val != p.val:
                return False
            p = p.next
        return True

``` 




