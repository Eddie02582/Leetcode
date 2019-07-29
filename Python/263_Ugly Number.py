class Solution(object):
    def isUgly(self, num):
        if num == 0 :
            return 0
        factors = [2,3,5]
        for n in factors:
            while num % n ==0:
                num //= n

        return 1 == num