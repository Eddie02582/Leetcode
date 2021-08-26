from math import sqrt
class Solution:
    def judgeSquareSum_hash_set(self, c: int) -> bool:
        squares = set()
        for i in range(0,int(c**0.5)+1):
            squares.add(i * i)
        
        for square in squares:
            if (c - square) in squares:
                return True           
        return False 


    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = sqrt(c - a * a);
            if b == int(b):
                return True  
            a += 1
        return False 
        
        
    def judgeSquareSum(self, c: int) -> bool:
        l,r = 0, int(c **0.5)
        while l <= r:
            value = l * l + r * r
            if value == c:
                return True
            elif value > c:
                r -= 1
            else:
                l +=1  
        return False 
        
        