'''
Given two arrays, write a function to compute their intersection.

Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]
    
Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.

'''

class Solution(object):
    def intersection_list(self, nums1, nums2):
        result = [] 
        for n in nums2:
            if n in nums1 and n not in result:
                result.append(n)
        return result
        
    def intersection(self, nums1, nums2):
        result = set()
        for n in nums2:
            if n in nums1:
                result.add(n)
        return list(result)

    def intersection(self, nums1, nums2):      
        return list(set(nums1) & set(nums2))