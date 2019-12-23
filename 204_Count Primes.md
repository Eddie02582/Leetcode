# Two Sum


## 原題目:
```
Count the number of prime numbers less than a non-negative number, n.

Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
```

## 思路1
典型sieve of Eratosthenes 題目,在一定範圍內找出質數,建立一個長度為n陣列皆為True,迴圈從2開始到n,其原理是2是質數,則4,6,8..到n之前,2的倍數皆不是質數<br>
所以j從  range(i + i,n,i) ,下面解法是進階的j從 i x i開始,因為再前面過濾的時候會重複,可以直接從 i x i開始


#### Python

``` python
class Solution:
    def countPrimes(self, n: int) -> int:
        Isprime = [ True for i in range(n)]
        count = 0
        for i in range(2,n):
            if Isprime[i]:
                count += 1
                for j in range(i * i,n,i):
                    Isprime[j] = False
        return count    
``` 






