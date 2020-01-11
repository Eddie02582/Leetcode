# Merge Sorted Array


## 原題目:
```
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

## 思路1
1.將nums2 値放入nums1 索引値m 到 m + n - 1
2.排序即可

## Code

#### Python

``` python
class Solution(object):
    def merge_cheating(self, nums1, m, nums2, n):       
        nums1[m:] = nums2
        nums1.sort()
```  

## 思路2

1. 利用雙指針m,n 記錄目前個數
2. 比較nums1[m] 和nums2[n]値,若m = 0 or n > 0 且nums2[n - 1] > nums1[m - 1],把nums1[n + m - 1] = nums2[n - 1],並將n =n - 1,反之[n + m - 1] = nums2[m - 1],m -= 1




## Code

#### Python


``` python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        while n or m :
            if  not m or  (n  and nums2[n - 1] > nums1[m - 1]):
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1            
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
   
        
```  


解化上面,當m = 0,表示陣列以排完


``` python
class Solution(object):
    def merge(self, nums1, m, nums2, n): 
        while n:
            if  not m  or  nums2[n - 1] > nums1[m - 1]:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1            
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
   
        
```  

















