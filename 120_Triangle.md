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

可使用zip 就不需判斷陣列索引値是否會超過

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        strs.sort()
        s  = ""
        for k,v in zip(strs[-1],strs[0]):
            if k != v:
                break
            s += k 
        return s
```

#### js
```javascript
var longestCommonPrefix = function(strs) {
    if (strs.length == 0)
        return "";
    else if (strs.length == 1 )
        return strs[0];    
    
    strs.sort();
    var p = 0 , lastindex = strs.length - 1
    var s = ""  
    while (p < strs[0].length && p < strs[lastindex].length){
        if (strs[0][p] != strs[lastindex][p]){
            break
        }
        s += strs[0][p++]     
    }   
    
  
    return s;
};

```

## 思路2
直覺得做法,一一比對每個陣列的字串値


## Code

#### Python

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ""   
        msg,s="",strs[0]	
        
        for i in range(1,len(s)+1):
            if  all ( s[:i]== p[:i] for p in  strs):
                msg=s[:i]
            else:
                break
        return msg    
  
```








