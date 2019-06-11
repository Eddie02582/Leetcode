'''

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

    Input: 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
Example 2:

    Input: 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step

'''
#!/usr/bin/python
# encoding=utf-8

##http://www.csie.ntnu.edu.tw/~u91029/DynamicProgramming.html

class Solution(object):
       
    #分析從0開始每一階階有1步或2步的選擇
    def climbStairs_BruteForce(self, n):  
        return self.climb_Stairs_BruteForce(0,n)
        
    def climb_Stairs_BruteForce(self, i,n):
        if i > n:
            return 0
        if i==n :
            return 1            
        return self.climb_Stairs_BruteForce(i + 1, n) + self.climb_Stairs_BruteForce(i + 2, n);
    
    
    #爬到五階」的踏法數目，就是總合「爬到四階」與「爬到三階」的踏法數目
    #直接用遞迴實作,時間複雜度是 O(f(n)) 
    def climbStairs(self, n):  
        if n==0 or n==1:
            return 1
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2);
        
  
         
    #上面的進階寫法,使用記憶體儲存各個問題的答案    
    #Top-down 由後往前 5=3+4 
    #                    -->4=3+2,3=2+1
   
    
    def climbStairs_top_down(self, n):  
        table=[0]*(n+1)
        if n==0 or n==1:
            return 1
            
        if table[n] !=0:
            return table[n]
            
        table[n]=  self.climbStairs_top_down(n-1) + self.climbStairs_top_down(n-2)
        return table[n]    
    
    
    
    ## Bottom-up  
    def climbStairs_Bottom_up(self,n):       
            
        table=[0]*(n+1) 
        table[1]=1
        table[2]=2
        for i in range(3,n+1):
            table[i]=table[i-1]+table[i-2]

        return table[n]

    def climbStairs_Dynamic(self,n):
        table=[0]*(n+1)    
        table[0]=1
 
        for i in range(0,n+1):
            if i+1 <=n:
                table[i+1]+= table[i]
            if i+2 <=n:
                table[i+2]+= table[i]
        return table[n]



sol =Solution()

assert sol.climbStairs_BruteForce(3) == 3

assert sol.climbStairs(3) == 3

assert sol.climbStairs_Bottom_up(3) == 3

assert sol.climbStairs_Dynamic(3) == 3











    