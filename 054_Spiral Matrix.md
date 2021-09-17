# Spiral Matrix

## 原題目:
```
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

    Input:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    Output: [1,2,3,6,9,8,7,4,5]
Example 2:

    Input:
    [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9,10,11,12]
    ]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]
```

## 思路1
移動順序右下左上,當碰壁或是以拜訪過的位置,則回上一個位置,往下一個移動順序前進

#### Python

``` python
class Solution(object):
    def spiralOrder(self, matrix):   
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        loc = 0
        visited = set()
        ans = []
        m,n = len(matrix),len(matrix[0])
        row,col = 0,0
        while len(ans) < m * n:
            ans.append(matrix[row][col]) 
            visited.add((row,col))   
            
            new_row,new_col = row + directions[loc][0],col + directions[loc][1]
            
            if new_row < 0 or new_row >= m or new_col < 0 or new_col >= n or (new_row,new_col) in visited:            
                loc = (loc + 1)%4
            
            row += directions[loc][0]
            col += directions[loc][1]
        
        return ans 
``` 




