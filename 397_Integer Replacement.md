# Integer Replacement


## 原題目:
```
Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

 

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2
```

## 思路bfs

#### Python

``` python
class Solution(object):        
    def integerReplacement(self, n: int) -> int:
        from collections import deque
        queue = deque([n])        
        
        level = 0
        while queue:
            length = len(queue)            
            for i in range(length):
                node = queue.popleft()
                if node == 1:
                    return level           
                elif node % 2:
                    queue += [node + 1,node - 1]
                else:
                    queue.append(node//2)               
            level += 1      
        
        return -1 
``` 

## 思路dfs


#### Python


``` python
class Solution(object):    
    def integerReplacement(self, n: int) -> int:        
        def dfs(node):           
            if node == 1:                
                return 0         
            if node % 2:
                return min(dfs(node + 1),dfs(node - 1)) + 1
            else:
                return dfs(node // 2) + 1   
        return  dfs(n)  
``` 



