#  Pascal's Triangle


## 原題目:
```
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
```

## 思路1 



## Code



#### Python

```python
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        output = []
        for i in range(numRows):
            rowdata = []
            for  j in range(i + 1):
                if j == 0 or j == i:
                    rowdata.append(1)
                else:   
                    rowdata.append(output[i -1][j - 1] + output[i -1][j])
            output.append(rowdata)
        return output
```








