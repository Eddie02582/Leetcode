# Triangle


## 原題目:
```
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
```

## 思路1 分治法



## Code



#### Python

```python
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """        

        def dfs (x,y,triangle):
            n = len(triangle)
            if x == n:               
                return 0
            return min(dfs(x + 1, y, triangle), dfs(x + 1, y + 1, triangle)) + triangle[x][y]
     
        if not triangle:
            return -1
        
        result = dfs (0,0,triangle)
        return result
```


## 思路2 
由底部往前

```python
class Solution(object):
    def minimumTotal_bottom_to_top(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None
        elif len(triangle) == 1:
            return triangle[0][0]
               
        p = len(triangle) - 2
       
        while p >= 0:
            for i in range(len(triangle[p])):
                triangle[p][i] += min(triangle[p + 1][i],triangle[p + 1][i + 1])
            p -= 1
        
        return triangle[0][0]
```

## 思路ˇ 
由上往下
```python
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return None 
               
        p = 1
       
        while p <  len(triangle):
            for i in range(p + 1):
                if i == 0 :
                    triangle[p][i] += triangle[p-1][0]
                elif i == p:
                    triangle[p][i] += triangle[p-1][-1]
                else:
                    triangle[p][i] += min(triangle[p - 1][i - 1],triangle[p - 1][i])
            p += 1
        
        return min(triangle[-1])   
```


