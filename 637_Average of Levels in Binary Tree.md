# Average of Levels in Binary Tree

## 原題目:
```
Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
    3
   / \
  9  20
    /  \
   15    7
Input: root = [3,9,20,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].
Example 2:


Input: root = [3,9,20,15,7]

    3
   / \
  9  20
 /  \
15   7

Output: [3.00000,14.50000,11.00000]
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
 
```

## 思路bfs



#### Python
``` python
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from collections import deque
        if not root:return []
        queue = deque([root])      
        ans = []
        while queue:
            length = len(queue)
            value  = 0
            for i in range(length):
                node = queue.popleft()                
                value += node.val
                if node.left:queue.append(node.left)
                if node.right:queue.append(node.right)
            
            ans.append(value/length)
        return ans
``` 




#### c++
```c++
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        vector<double> averages; 
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()){
            int size = q.size();
            double sum = 0;
            for(int k = 0;k < size;k++){
                TreeNode *node = q.front();
                q.pop();
                sum += node->val;
                if(node->left)
                    q.push(node->left);
                if(node->right)
                    q.push(node->right);
            }           
            averages.push_back(sum/size);  
        }
        return averages;
    }
};



```










