# Binary Tree Inorder Traversal


## 原題目:
```
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
```

## 思路遞回


## Code

#### Python

``` python
class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def hepler(root,result):
            if root:
                hepler(root.left,result)
                result.append(root.val)
                hepler(root.right,result)        
            return result
        
        return hepler(root,[])    
```  

#### c++
```c++
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        if (root == NULL)
            return {};

        vector<int> ans ;
        traverse(root,ans);
        return ans;
        
    }
    
    void traverse(TreeNode* root,vector<int> &ans ) {
        if (root == NULL)
            return ;   
        traverse(root->left,ans);
        ans.push_back(root->val);
        traverse(root->right,ans);        
    } 
}
```



## 思路分治法


## Code

#### Python

``` python
class Solution(object):
    
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """   
        if root is None:            
            return []
        else:            
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)        
```  

## 思路stack


``` python
class Solution(object):
    
    def inorderTraversal_iterative(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        visited = set()
        if not root:
            return res
        queue = [root]
        while queue:
            curr = queue.pop()
            if curr not in visited:
                visited.add(curr)
                if curr.right:
                    queue.append(curr.right)
                queue.append(curr)
                if curr.left:
                    queue.append(curr.left)
            else:
                res +=[curr.val]
        return res   
        
    def inorderTraversal_iterate(self, root):
        result = []
        s = []
        while root or s:                     
            if root :
                s.append(root)
                root = root.left
            else:
                root = s.pop()
                result.append(root.val)
                root = root.right
        return result         
```  

#### c++
```c++
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) 
    {
        stack<TreeNode*> stk ; 
        vector<int> inorder ;
        TreeNode* node = root ;
        
        while(true)
        {   
            if(node != NULL)
            {
                stk.push(node); 
                node = node->left ;
            }
            else{
                if(stk.size() == 0)
                    break ;
                node = stk.top() ; 
                stk.pop() ;
                inorder.push_back(node->val);
                node = node->right ;
            }
               
        }
        return inorder;
    }
    
};




```












