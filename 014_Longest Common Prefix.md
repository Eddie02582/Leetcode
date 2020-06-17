# longestCommonPrefix


## 原題目:
```
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

    Input: ["flower","flow","flight"]
    Output: "fl"
    
 Example 2:

    Input: ["dog","racecar","car"]
    Output: ""
Explanation: There is no common prefix among the input strings.
```

## 思路1
將陣列排序並比較頭尾即可


## Code

#### Python

```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        s , p  = "",0
        while p < len(strs[-1]) and p < len(strs[0]):
            if strs[-1][p] != strs[0][p]:
                break
            s += strs[0][p]
            p += 1
        return s
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


## 思路3
Divide and conquer

## Code

#### Python
<a href = "https://github.com/Eddie02582/Algorithm/blob/master/Algorithm/Divide/Longest%20Common%20Prefix/README.md">參考</a>



```python
class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]          
        
        def helper(str1,str2):
            p = 0
            s = ""
            while p < len(str1) and  p <len(str2):
                if str1[p] != str2[p]:
                    break              
                s += str1[p]
                p += 1            
            return s
                
        
        mid = len(strs)//2
        left = strs[:mid]
        right = strs[mid:]
        left = self.longestCommonPrefix(left)
        right = self.longestCommonPrefix(right)
        s = helper(left,right)
        return s
        

sol = Solution()
input = ["geeksforgeeks", "geeks", "geek", "geezer"]
sol.longestCommonPrefix(input)

```






