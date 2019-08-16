'''
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:

    n = 5

    The coins can form the following rows:
    ?
    ? ?
    ? ?

    Because the 3rd row is incomplete, we return 2.
Example 2:

    n = 8

    The coins can form the following rows:
    ?
    ? ?
    ? ? ?
    ? ?
'''

class Solution(object):
    def arrangeCoins(self, n):
        total,count,i = 0 ,0,1     
        
        while True:
            total += i
            i += 1
            if total > n:
                break
            count += 1
        return count

    def arrangeCoins_row(self, n: int) -> int:
        row = 1
        while n >= row:
            n -= row
            row += 1
        
        return row - 1
    
def arrangeCoins(self, n: int) -> int:

    if(n<0):
        return -1
    return int((-1+ (1+8*n)**0.5)//2)
       


sol = Solution()
assert sol.arrangeCoins(5) ==  2 

assert sol.arrangeCoins(8) ==  3 

assert sol.arrangeCoins(1) ==  1 
