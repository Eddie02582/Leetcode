'''
Given an array of integers, 1 ? a[i] ? n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

Example:
Input:
[4,3,2,7,8,2,3,1]

Output:
[2,3]

'''

class Solution(object):
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
        
    def findDuplicates_dict(self, nums):
        from collections import Counter
        count = Counter(nums) 
        return  [ key for key,value in count.items() if value == 2 ]
        

    def findDuplicates_non_extra(self, nums):
        ans = []
        for num in nums:
            if nums[abs(num) - 1] < 0:
                ans.append(abs(num))
            nums[abs(num) - 1] *= - 1
        return ans


sol = Solution()
sol.findDuplicates_non_extra([4,3,2,7,8,2,3,1])