# Daily Temperatures

## 原題目:
```
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
```

## 思路暴力解


#### Python
``` python
class Solution(object):
    #timeout
    def dailyTemperatures_(self, T):
        array = [0]*len(T)
        for i in range(0,len(T)):
            for j in range(i+1,len(T)):
                if T[j] > T[i]:
                    array[i] = j - i
                    break
        return array

```


## 思路stack
T = [73, 74, 75, 71, 69, 72, 76, 73]<br>
假設這個是身高,從T[0]的角度往右看只會看到[74,75,76],矮的會被前面大的檔住,這邊用堆疊的方式反過來存成嚴格遞減的陣列([76,75,74]),因為要計算index 差,所以用[T[i],i]方式儲存<br>
由後往前處理,當歷遍到i,需要stack pop,直到T[i] < stack[-1][0],此時stack[-1]就是下一個比它大的值,記錄index 差<br>


#### Python
``` python
class Solution(object):
    def dailyTemperatures_(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
       
        ans = [0] * len(T)
        stack = []
        for i in range(len(T) - 1,-1,-1):
                # remove index > i and smaller temperture 
            while stack and stack[-1][0] <= T[i]:
                stack.pop()
            if stack:                
                ans[i] = stack[-1][1] - i 
            stack.append([T[i],i])
        
        return ans

```

## 思路 stack由前往後
這邊的思路排隊的概念,當後進來的比陣列最前面大,前面的就移除



``` python

class Solution(object):        
    def dailyTemperatures(self, T):
        N = len(T)
        stack = []
        res = [0] * N
        for i, t in enumerate(T):
            while stack and stack[-1][0] < t:
                oi = stack.pop()[1]
                res[oi] = i - oi
            stack.append((t, i))
        return res    

```








