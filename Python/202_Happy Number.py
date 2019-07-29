class Solution:
    def isHappy(self,n):    
        set_num = set()
        while n != 1:
            n = self.getsum(n)
            if n in set_num:
                return False
            set_num.add(n)           
            
        return True 
    
    def getsum(self,n):
        total = 0
        while n:
            total = total + (n%10)**2
            n = n//10
        return total