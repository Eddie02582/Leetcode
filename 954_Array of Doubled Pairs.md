# Array of Doubled Pairs


## 原題目:
```
Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.
 

Example 1:
	Input: arr = [3,1,3,6]
	Output: false
	
Example 2:
	Input: arr = [2,1,2,6]
	Output: false
	
Example 3:
	Input: arr = [4,-2,2,-4]
	Output: true
	Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
	
Example 4:
	Input: arr = [1,2,4,16,8,4]
	Output: false
 

Constraints:

2 <= arr.length <= 3 * 104
arr.length is even.
-105 <= arr[i] <= 105

```

## 思路

```
先計算所有個數,排序依照abs排序,如果已經配對過了個數減一,如果配不對回傳False


```


#### Python
``` python
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        from collections import Counter       
        arr.sort(key = lambda x:abs(x))
        counts = Counter(arr)        
        
        for n in arr:
            if counts[n] > 0:
                if counts[2 * n] <= 0:
                    return False           
                counts[n] -= 1
                counts[2 * n] -= 1            
                
        return True
``` 












