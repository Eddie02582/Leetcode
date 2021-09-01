'''

We define a harmounious array as an array where the difference between its maximum value 
and its minimum value is exactly 1.

Now, given an integer array, you need to find the length of its longest harmonious subsequence 
among all its possible subsequences.

Example 1:

    Input: [1,3,2,2,5,2,3,7]
    Output: 5
    Explanation: The longest harmonious subsequence is [3,2,2,2,3].

Note: The length of the input array will not exceed 20,000.

'''

class Solution(object):

    def findLHS(self, nums):        
        from collections import Counter
        count = Counter(nums)
        
        longest = 0
        for key in count.keys():
            if key + 1 in count:
                longest = max (longest,count[key] + count[key + 1])           
        return longest




            

sol = Solution()
assert sol.findLHS([1,3,2,2,5,2,3,7]) == 5

assert sol.findLHS([-1,0,-1,0,-1,0,-1]) == 7