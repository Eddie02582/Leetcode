'''
Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

    Input: n = 10
    Output: 12
    Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
'''
import heapq
class Solution(object):
    def nthUglyNumber_dict(self, n):
        dict = {1:True} 
        count = 0
        factor = [2,3,5]
        i = 0
        while count < n:  
            i += 1
            if dict.get(i,False):
                for f in factor:                    
                    dict[i*f] = True                    
                count += 1
        return i
        
    def nthUglyNumber_set(self, n):
        hashset = set([1]) 
        count = 0
        factor = [2,3,5]
        i = 0
        while count < n:  
            i += 1
            if i in hashset:
                for f in factor:                     
                    hashset.add(i*f)                  
                count += 1
        return i

    def nthUglyNumber_heapq(self, n):
        heap = [1]
        visited = set([1])
        
        for i in range(n):
            val = heapq.heappop(heap)
            
            for factor in [2,3,5]:
                if val*factor not in visited:
                    heapq.heappush(heap, val*factor)
                    visited.add(val*factor) 
        return val

        
    def nthUglyNumber(self, n):
        ugly = [1]
        i2 = i3 = i5 = 0
        while len(ugly) < n:
            m2,m3,m5 = ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5
            mn = min(m2, m3, m5)
            if (mn == m2): 
                i2 +=1 
            if (mn == m3): 
                i3 += 1
            if (mn == m5): 
                i5 += 1
            ugly.append(mn);        
        return ugly[-1]        
        
        
    def nthUglyNumber_timeout(self, n): 
        count = 0 
        i = 0
        while count < n :
            i += 1
            if self.isUgly(i):
                count += 1           
        return i
        
    def isUgly(self, num):
        if num == 1 :
            return True
        factors = [2,3,5]
        for n in factors:
            while num % n ==0:
                num //= n

        return 1 == num        
       
sol =Solution()
print (sol.nthUglyNumber(446))
        
print (sol.nthUglyNumber_timeout(446))        
        

        
        
        
        
                