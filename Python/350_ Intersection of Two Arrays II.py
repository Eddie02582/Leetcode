'''
iven two arrays, write a function to compute their intersection.

Given two arrays, write a function to compute their intersection.

Example 1:

    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]
Example 2:

    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.

'''

'''
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
'''

class Solution(object):
    def intersect(self, nums1, nums2):
        dict = {}
        result = []        
        for n in nums2:            
            dict[n] = dict.get(n,0) + 1            
        for n in nums1:
            if dict.get(n,0) :
                dict[n] -= 1
                result.append(n)
        return result

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        n1_count = Counter(nums1)
        n2_count = Counter(nums2)        
        ans = []        
        for key in n1_count.keys():
            if key in n2_count:
                ans += [key] * min(n1_count[key],n2_count[key])        
        return ans

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        return sum([[k] * v for k, v in (counter1 & counter2).items()], [])