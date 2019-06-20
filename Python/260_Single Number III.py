'''
Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.

Example:

    Input:  [1,2,1,3,2,5]
    Output: [3,5]
    Note:

The order of the result is not important. So in the above example, [5, 3] is also correct.
Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?

'''

#!/usr/bin/python
# encoding=utf-8
class Solution(object):
    def singleNumber_counter(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        counter=Counter(nums)
        return [ key for key in counter.keys() if counter[key]==1 ]
        
 
    
    #136_Single Number加强版的题目，也會很自然的想到 xor 一遍，假设只出现一次的兩個数是 A、B，最後只能得到值 = A xor B，但没有辦法知道 A 是多少，B 是多少。
    #那得到的這個值有沒有用呢？有，xor 是按位比較，相同為0，不同為1，也就是說得到的這個值裡，所有的1都代表了：在這個位置上，A 和B 是不同的，這給我們區分AB 提供了一個方法：
    ##我們隨便找一個是1的位置（也就是A和B 在這個位置上的值反正有一個是0 有一個是1），再次遍歷一遍數組，按照這個位置上是0還是1分成兩組，那麼A 和B 一定會被分開。而對於其他的數字，無論他們在這個位置上是0還是1，總之他們會兩兩一對分到兩個組中的任意一個組裡去。
    #這就轉化成了初級版本的問題了，每個組中都只有一個數出現1次，對兩個組分別做一次xor ，得到兩個數就是 A 和 B。
    

    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        combined =0
        for num in nums:
            combined ^= num            
       
        index=0
        number1 ,number2 = 0 ,0        
        for i in range(0,32):
            if combined >> i & 1 == 1:
                index = i
                break
                
        for num in nums:
            if num  >> i & 1 == 1:
                number1 ^=num
            else:
                number2 ^=num
                
                
        return  [number1,number2]      
                
                
                
        
sol =  Solution()
assert sol.singleNumber([1,2,1,3,2,5])==[3,5]