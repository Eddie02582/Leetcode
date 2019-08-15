'''
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]
Example 2:

    Input: nums = [1], k = 1
    Output: [1]
    Note:

You may assume k is always valid, 1 ? k ? number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


'''

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]        
        """
        count = {}
        for n in nums:
            count[n] =count.setdefault(n,0) + 1
        
        return sorted(count.keys(), key=lambda kv: -count[kv])[0:k]
        
    def topKFrequent_counter(self, nums, k):
        from collections import Counter
        count = Counter(nums)     
        return sorted(count.keys(), key=lambda kv: -count[kv])[0:k]
        #return sorted(count.keys(), key=count.get,reverse=True)[0:k]        
        
        
        
        
        
        
        
        
        
        
        
        
        