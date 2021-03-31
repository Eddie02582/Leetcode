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

## 思路 分治法



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


## 思路 動態規劃
由底部往前

#### Python
```python
class Solution(object):
    def minimumTotal_bottom_to_top(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        if not triangle:
            return 0
        n = len(triangle)
        
        for i in range(n - 2,-1,-1):
            for j in range(0,i + 1): 
                triangle [i][j] += min(triangle [i + 1][j],triangle [i + 1][j + 1])                
 
        return triangle[0][0]        
        
```

#### C#
```csharp
public class Solution {

    public int MinimumTotal(IList<IList<int>> triangle) { 
        //down-top
        int m = triangle.Count();
        for (int row = m - 2;row >= 0;row--){
            for(int col = 0;col <triangle[row].Count();col ++){
                triangle[row][col] += Math.Min(triangle[row + 1][col],triangle[row + 1][col + 1]);
            }
        }
        return triangle[0][0];
    }

}
```

## 思路 動態規劃由上往下 
#### Python
```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)        
        for i in range(1,n):
            m = len(triangle[i])
            for j in range(0,m):
                if j == 0:
                    triangle [i][j] += triangle [i - 1][0]
                elif j == m - 1:
                    triangle [i][j] += triangle [i - 1][-1]
                else:
                    triangle [i][j] += min(triangle [i - 1][j - 1],triangle [i - 1][j])                   
        
        return min(triangle[-1])
```

#### C#
```csharp
public class Solution {

    public int MinimumTotal(IList<IList<int>> triangle) {        
        //top-down
        int m = triangle.Count();
        for (int i = 1; i < m; i++)
        {
            for (int j = 0; j < triangle[i].Count(); j++)
            {
                if (j == 0)
                {
                    triangle[i][j] += triangle[i - 1][0];
                }
                else if (j == triangle[i - 1].Count())
                {
                    triangle[i][j] += triangle[i - 1][j - 1];
                }
                else
                {
                    triangle[i][j] = triangle[i][j] + Math.Min(triangle[i - 1][j - 1], triangle[i - 1][j]);
                }
            }

        }

        return triangle[m - 1].Min();
    }

}
```











