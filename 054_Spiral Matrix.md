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
        if matrix == []:
            return []
            
        row,col,count=0,0,0
        len_row ,len_col =len(matrix) ,len(matrix[0])    
        col_step ,row_step =[1,0,-1,0],[0,1,0,-1] 
        visted = [[ False for i in range(len_col)] for j in range(len_row)]
        output=[]         
        
        while len(output) < len_row * len_col:

            if  0 <= row < len_row and  0 <= col < len_col and not visted[row][col]:            
                output.append( matrix[row][col])
                visted[row][col] = True
            else:
                row -= row_step[count]
                col -= col_step[count] 
                count = ( count + 1 )  % 4

            row += row_step[count]
            col += col_step[count]  
                
        return output   
``` 

## 思路1
 
用i歷遍整個陣列,當總合為負値表示需要重新計算,

#### Python
```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        temp = 0
        for n in nums:            
            temp += n
            res = max(res,temp)
            if temp < 0:
                temp = 0
        return res
```




