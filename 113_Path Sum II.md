#  Path Sum II


## 原題目:
```
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]  1
```

## 思路
同path sum 只是多記錄了結果


## Code

#### Python

這邊很奇怪使用path = path + [node.val]  會回朔,但是path+= [node.val]就不會
```python
class Solution:
    def pathSum(self, root: TreeNode, targetSum):
        ans = []        
        
        def backtracking(node,path,path_res): 
            if not node:
                return 
            path = path + [node.val]             
            path_res -= node.val 
            if (not node.left and not node.right and path_res == 0):
                ans.append(path[::])
             
            backtracking(node.left,path,path_res)
            backtracking(node.right,path,path_res)

        backtracking(root,[],targetSum)
        return ans 
```

```python
class Solution:
    def pathSum(self, root: TreeNode, targetSum):
        ans = []  
        def backtracking(node,path,path_res):
            if not node:
                return             
            path +=[node.val]  
            path_res -= node.val         
            if not node.left and not node.right and path_res == 0:
                ans.append(path[:])
            else:
                backtracking(node.left,path,path_res)
                backtracking(node.right,path,path_res)                 
            path.pop(-1)



        backtracking(root,[],targetSum)
        return ans

```

#### C#

```csharp
 public class Solution {
        public IList<IList<int>> PathSum(TreeNode root, int targetSum)
        {
            IList<IList<int>> ans = new List<IList<int>>();            
            getPathSum(root, targetSum, new List<int>(), ans);
            return ans;
        }

        public void getPathSum(TreeNode node, int path_res, IList<int> path, IList<IList<int>> ans)
        {                        
            if (node == null)
                return;

            path.Add(node.val);
            path_res = path_res - node.val;
            if (node.left != null)
            {
                getPathSum(node.left, path_res , path, ans);  
                path.RemoveAt(path.Count() - 1);
               
            }
            if (node.right != null)
            {
                getPathSum(node.right, path_res, path, ans);               
                path.RemoveAt(path.Count() - 1);
            }

            if (node.left == null && node.right == null)
            {
                if (path_res == 0)
                    ans.Add(new List<int>(path));
            }
        }

}
```
使用new List<int>(path) 就不需要path.RemoveAt(path.Count() - 1)的回朔動作,因為傳入的是新物件

```csharp
 public class Solution {
        public IList<IList<int>> PathSum(TreeNode root, int targetSum)
        {
            IList<IList<int>> ans = new List<IList<int>>();            
            getPathSum(root, targetSum, new List<int>(), ans);
            return ans;
        }

        public void getPathSum(TreeNode node, int path_res, IList<int> path, IList<IList<int>> ans)
        {                        
            if (node == null)
                return;

            path.Add(node.val);
            path_res = path_res - node.val;
            if (node.left != null)          
                getPathSum(node.left, path_res , new List<int>(path), ans);   
            if (node.right != null)         
                getPathSum(node.right, path_res, new List<int>(path), ans);
                
            if (node.left == null && node.right == null && path_res == 0) 
                ans.Add(path);
           
        }

}
```





