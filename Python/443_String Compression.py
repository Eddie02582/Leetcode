'''
Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.

 
Follow up:
Could you solve it using only O(1) extra space?

 
Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".
'''

class Solution(object):
    def compress(self, chars):        
        index = 0
        p = chars[0]
        count = 1 
        for s in chars[1:]:
            if s != p: 
                if  count != 1: 
                    for q in str(count):
                        index += 1
                        chars[index] = q
                index += 1 
                chars[index] = s 
                count,p = 1,s
            else:
                count += 1  
        if  count != 1:        
            for s in str(count):
                index += 1
                chars[index] = s

        return  index + 1
        
 
sol = Solution()
 
assert sol.compress(["a","a","b","b","c","c","c"]) == 6

assert sol.compress(["a"]) == 1

assert sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]) == 4