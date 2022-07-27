# Rotate List

## 原題目:
```
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
    Input: head = [1,2,3,4,5], k = 2    
                1 -> 2 -> 3 -> 4 -> 5
    Rotate 1    5 -> 1 -> 2 -> 3 -> 4
    Rotate 2    4 -> 5 -> 1 -> 2 -> 3         
    
    Output: [4,5,1,2,3]
Example 2:
    Input: head = [0,1,2], k = 4
                0 -> 1 ->2 
                
    Rotate 1    2 -> 0 ->1 
    Rotate 2    1 -> 2 ->0 
    Rotate 3    0 -> 1 ->2 
    Rotate 4    2 -> 0 ->1 

```




## 思路 動態規劃
[1,2,3,4,5],k = 2為例,需要拆成[1,2,3]和[4,5]然後對掉<br>

1.先找到LinkLids長度,找到LinkLids長度-k 的位置(第三個位置),將3的下一個當成新的newhead,並將3指向NULL<br>
2.再將最尾巴指向原本的頭(head)


####  C++

```c++
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
    ListNode* rotateRight(ListNode* head, int k) {
        if ( k == 0 || head == NULL)
            return head;        
       
        //find ListNode Length
        ListNode* p = head;
        int linkLength = 1; 
        
        while (p ->next != NULL){
            p = p->next;
            ++linkLength;
        }             
        //not need rotate
        if(k % linkLength == 0)
            return head;
        
        //find rotate prev item
        int cutLocation = linkLength -k % linkLength - 1;    
        ListNode* q = head;        
        while (cutLocation--){           
            q = q->next;  
        }     
        
        //new head equql cut item next        
        ListNode *newHead = q->next;
        q->next = NULL;
        
        // new head last item need to pointer to head    
        p->next = head;        
        return newHead; 
    }
};
```
