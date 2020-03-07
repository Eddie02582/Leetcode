# Reverse Integer


## 原題目:
```
Given n non-negative integers a1, a2, ..., an , where each 
represents a point at coordinate (i, ai). n vertical lines are drawn 
such that the two endpoints of line i is at (i, ai) and (i, 0). 
Find two lines, which together with x-axis forms a container, 
such that the container contains the most water.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49
```

## 思路1
暴力解法,雙重迴圈i為左邊,j為右邊


## Code

#### Python

```python
class Solution(object):
    def maxArea(self, height):       
        max_area = 0
        length = len(height)
        for i in range(length):
            for j in range(i + 1,length):
                h = min(height[i],height[j])
                area = (j - i) * h 
                max_area = max(max_area,area)
        return max_area
        
```


## 思路2
設定雙重指針l = 0 ,r = length - 1 ,因為面積為min(height[l],height[r])(r-l),所以
當height[l],height[r]較小值需要移動,改變值才能產生更大的面積


## Code

#### Python

```python
class Solution(object):        
    def maxArea(self, height):
        max_area = 0
        length = len(height)
        l,r = 0 ,length - 1 
        
        while l < r :
            h = min(height[l],height[r])
            area = (r - l) * h
            max_area = max(max_area,area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1  
            
        return max_area
```








