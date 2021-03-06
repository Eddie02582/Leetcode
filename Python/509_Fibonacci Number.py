'''

The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), for N > 1.


Given N, calculate F(N).

 

Example 1:

    Input: 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    
Example 2:

    Input: 3
    Output: 2
    Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
    
Example 3:

    Input: 4
    Output: 3
    Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.



'''

class Solution(object):
    def fib_res(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
            
        return self.fib(N-2)+self.fib(N-1)

    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1        
        table=[0]*(N+1)
        table[1]=1
        
        for i in range(2,N+1):
            table[i]=table[i-1]+table[i-2]
       
        return table[N]