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
        
    def isHappy_res(self, n: int) -> bool:
        isExist = set()         
        def helper(num):       
            if num == 1:
                return True  
            elif num in isExist:
                return False
            isExist.add(num)
            num = sum(map(lambda x:int(x)**2,str(num)))
            return helper(num)
        
        return helper(n)