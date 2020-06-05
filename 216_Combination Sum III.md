# Count Primes


## 原題目:
```
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

    Input: k = 3, n = 7
    Output: [[1,2,4]]
Example 2:

    Input: k = 3, n = 9
    Output: [[1,2,6], [1,3,5], [2,3,4]]
```

## 思路backtracking
基本上就是backtracking



#### Python

``` python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:          
        
        def backtracking(array,start,target):
            if target == 0 and len(array) == k:
                res.append(array[:])
                return        
            elif target < 0  or len(array) > k:
                return   
            for i in range(start,10):  
                backtracking(array + [i], i + 1 ,target - i)
                   

        res = []
        backtracking([],1,n)
        return res

``` 

這邊簡化一下範圍,當n < 9 時可以調整迴圈的範圍


``` python
class Solution:
    def combinationSum3(self, k,n):     
        
        def backtracking(array,start,target):
            if target == 0 and len(array) == k:
                res.append(array[:])
                return        
            elif target < 0  or len(array) > k:
                return   
            for i in range(start,end):  
                backtracking(array + [i], i + 1 ,target - i)
                   

        res = []
        end = 10
        if n < end:
            end = n + 1

        backtracking([],1,n)
        return res   
``` 






