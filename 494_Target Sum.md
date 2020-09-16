# Target Sum


## 原題目:
```
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. 

Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.

Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:

Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5
Explanation: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
 

Constraints:

The length of the given array is positive and will not exceed 20.
The sum of elements in the given array will not exceed 1000.
Your output answer is guaranteed to be fitted in a 32-bit integer.
```

## 思路backtracking



#### Python
歷遍nums元素,每次可以選擇+/-,如果歷遍結束和與s相同就符合


``` python
class Solution(object):
    def findTargetSumWays__(self, nums, S):
        def backtracking(s,total):
            if s == len(nums):
                if total == S:
                    self.ans += 1
                return
                
            backtracking(s + 1,total + nums[s])
            backtracking(s + 1,total - nums[s])
            
        backtracking(0,0)       
        return self.ans    
``` 

簡化搭配dict


``` python
class Solution(object):        
    def findTargetSumWays(self, nums, S):
        self.ans = 0
        memo = {}
        def backtracking(s,total):
            if s == len(nums):
                if total == S:
                    return 1
                return 0
                
            count = backtracking(s + 1,total + nums[s]) + backtracking(s + 1,total - nums[s])
            memo[(s,total)] = count
            return count
        
        return backtracking(0,0)   
``` 



## 思路 動態規劃

假設把nums,分成兩堆,A為+的和,B為-的和,可以得到下列式子
```
 A + B = sum
 A - B = S

=> A = (sum - S)//2

```
所以題目就變成在nums 的子集合找到和為A<br>
類似<href = "https://leetcode.com/problems/partition-equal-subset-sum/">Partition Equal Subset Sum</a>
dp[i][j],表示nums[0:i + 1]陣列,可以填滿j容量的方法總數<br>
dp[i][j],當下可以選擇num[i]或不選nums[i]<br>
如果不選 nums[i] 那么恰好方法数就取决于上一個狀態 dp[i-1][j]<br>
如果選 nums[i] ，把这第 i 个物品装入了背包，那麼只要看 dp[i-1][j-nums[i-1]]<br>
所以dp[i][j] = dp[i - 1][j] + dp[i-1][j-nums[i-1]]<br>

```
class Solution(object):        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if total < S or (total + S) % 2 == 1:
            return 0    
     
        n = len(nums)
        target = (total + S)//2        
        dp = [ [1 if  j== 0 else 0 for j in range(target + 1)] for i in range(n + 1)] 
      
        for i in range(1,n + 1):
            for j in range(target + 1):
                if j >= nums[i - 1]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]];
                else:
                    dp[i][j] = dp[i-1][j];
    
        return dp[n][target]     
```

由於每次只會用到前一次的狀態,可以簡化成一維陣列


```
class Solution(object):        
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        total = sum(nums)
        if total < S or (total + S) % 2 == 1:
            return 0    
     
        n = len(nums)
        target = (total + S)//2        
        dp = [0] * (target + 1)
        dp[0] = 1
      
        for i in range(1,n + 1):
            for j in range(target + 1,-1,-1):
                if j >= nums[i - 1]:
                    dp[j] = dp[j] + dp[j-nums[i-1]]
                else:
                    dp[j] = dp[j];
    
        return dp[target]        
```























