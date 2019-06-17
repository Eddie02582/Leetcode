'''
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    
Example 2:

    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

'''

#Note Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
class Solution(object):    
    def reverseString(self, s):
        l , r =0 , len(s)-1
        
        while l < r:
            s[l],s[r]=s[r],s[l]
            l += 1
            r -= 1
        #return (s)
        
    #slow
    def reverseString(self, s):        
        for i in range(len(s)):
            s.insert(i, s.pop())
        
    def reverseString(self, s):        
        for i in range(0,int(len(s)/2)):
            s[i],s[len(s)-1-i]=s[len(s)-1-i],s[i]
            
    def reverseString(self, s):        
        s.reverse()
 
 
sol =Solution()
#assert sol.reverseString2(["h","e","l","l","o"])==["o","l","l","e","h"]