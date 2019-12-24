# Find All Duplicates in an Array


## 原題目:
```
Given an array of integers, 1 ? a[i] ? n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]
```

## 思路1
假設不考慮without extra space 可以用dict統計各數,最後判斷出現次數為2的


#### Python

``` python
class Solution: 
    def findDuplicates(self, nums):
        from collections import Counter
        count = Counter(nums) 
        return  [ key for key,value in count.items() if value == 2 ])     
``` 

因為題目說只有出現1次或2次這兩種可能,亦也可以使用set 來判斷

``` python
class Solution:   
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        appear = set()
        result = []
        for n in nums:
            if n not in appear:
                appear.add(n)
            else:
                result.append(n)
        return result
```  




## 思路2

這個題的難點在於O(n)的時間複雜度和不用額外空間。題目給的一個trick,1 ≤ a[i] ≤ n，這樣使用a[i]-1把數組中該位置的元素求反，當再次遇到該位置時能夠通過這個位置是負數來確定出現了兩次。因為可能會對還沒有掃描到的位置進行求反，所以​​當掃描到該位置的時候應該進行求絕對值操作。

``` python
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= - 1
        return ans
``` 








