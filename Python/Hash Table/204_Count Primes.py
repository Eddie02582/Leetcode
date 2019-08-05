'''
Count the number of prime numbers less than a non-negative number, n.

Example:

    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

'''

class Solution(object):
    def countPrimes(self, n) :
        count, sieve = 0, [True] * n
        for i in range(2, n):
            if sieve[i]:
                count+=1
                for j in range(i*i, n, i):
                    sieve[j] = False
        return count



    def countPrimes__(self, n):
        count = 0
        for i in range (1,n):
            if isPrime(i):
                count += 1
        return count
    
    
def isPrime(n):
    if n <= 1:
        return False
                 
    end = int(n**0.5 + 1)
    for i in range (2,end):
        if n % i == 0:
            return False
    return True
        
sol = Solution()

assert sol.countPrimes(10) == 4