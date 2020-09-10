# Subsets

## 原題目:
```
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
```

參考
<a href = "https://leetcode.com/problems/subsets/solution/">Solution</a>

## 思路Cascading
在每一層output 再加上這層的選擇<br>

1. []<br>
2. output = [],choice = [1] => new_output = [],[1]<br>
3. output = [],[1],choice = [2] => new_output = [],[1],[2],[1,2]<br>
4. output = [],[1],[2],[1,2],choice = [3] => new_output = [],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]<br>

#### Python
``` python
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        output = [[]]
        
        for num in nums:
            temp = []
            for curr in output:
                temp.append(curr + [num])  
            output += temp
        return output
```



->[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]



## 思路backtrack


#### Python

這個思路是選0個到選n個
``` python
class Solution(object):
    def subsets(self, nums):      
        def backtrack(first = 0, curr = []):           
            if len(curr) == k:  
                output.append(curr[:])
            for i in range(first, n):               
                curr.append(nums[i])               
                backtrack(i + 1, curr)               
                curr.pop()
        
        output = []
        n = len(nums)
        for k in range(n + 1):
            backtrack()  
        return output

```
0:[]
1:[1],[2],[3]
2:[1,2],[1,3],[2,3]
3:[1,2,3]


->[[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

backtrack 的思路,每次都有選與不選的選擇

                
```            
1          []                  [1]
          /   \             /       \    
2        []   [2]        [1]       [1,2]
        / \   / \        / \       /    \
3     [] [3][2] [2,3]  [1] [1,3] [1,2] [1,2,3]

->[],[3],[2],[2,3],[1],[1,3],[1,2],[1,2,3]
```   

``` python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        if not nums:
            return []
        
        ans = []
        def backtracking(s,sol):
            if s == len(nums):
                ans.append(sol[:])
                return 
            backtracking(s + 1,sol)
            backtracking(s + 1,sol + [nums[s]]) 
        backtracking(0,[])        
        return ans

```

## 思路dfs
```

                []
          /      |      \
         /       |       \          
       [1]      [2]      [3]        
      /  \       |
   [1,2] [1,3]  [2,3]
    |
   [1,2,3]

->[],[1],[1,2],[1,2,3],[2],[2,3],[3]
```                  


``` python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:        
        if not nums:
            return []
        
        ans = []
        def dfs(s,sol):            
            ans.append(sol[:])            
            for i in range(s,len(nums)):                
                dfs(i + 1,sol + [nums[i]])  
        dfs(0,[])        
        return ans
```

## 思路bitmask


#### Python
``` python
class Solution(object):
    def subsets(self, nums):
        n = len(nums)
        output = []
        
        for i in range(2**n, 2**(n + 1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            
            # append subset corresponding to that bitmask
            output.append([nums[j] for j in range(n) if bitmask[j] == '1'])
        
        return output  
```







