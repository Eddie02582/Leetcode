class Solution:
    def hammingDistance(self, x, y):
        count=0
        for i in range(0,32):
            if x >> i & 1 != y >> i & 1:
                count += 1
        return count
        
    def hammingDistance(self, x, y):
        return bin(x^y).count('1')

    def hammingDistance(self,x, y):
            n = x ^ y
            h = 0
            while n:
                h += n & 1
                n >>= 1
            return h