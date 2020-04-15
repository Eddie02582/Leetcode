#  Pascal's Triangle


## 原題目:
```
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

    Input: 3
    Output: [1,3,3,1]

Follow up:

Could you optimize your algorithm to use only O(k) extra space?

```
## 思路1 
```
[k][0] :1
[k][1] :1 * k
[k][2] :1 * k * ( k - 1) / 2
[k][3] :[1 * k * ( k - 1) / 2 ] * ( k - 2 ) / 3
```

## Code



#### Python

```python
class Solution(object):
    def getRow(self, rowIndex):      
        res = []
        
        for i in range (rowIndex + 1):
            if i == 0 or i == rowIndex:
                res.append(1)
            else:
                res.append( res[-1] * ( rowIndex - i + 1) // i)
        return res
```


## 思路2
Dp
```python
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """    
        dp = [0] * (rowIndex + 1 )
        dp[0] = 1
        for i in range(1 ,rowIndex + 1):
            for j in range(rowIndex - 1,0,-1):
                dp[j] = dp[j] + dp[j - 1]
            dp[i] = 1
        return dp   

```


