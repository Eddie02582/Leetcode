'''
Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
'''
import collections
class Solution(object):
    def getHint(self, secret, guess):
        bulls,cows = 0,0
        dic_count = {}
        
        for p,q in zip(secret,guess):
            if p == q :                
                bulls += 1            
            else:
                dic_count[p] = dic_count.setdefault(p,0) + 1
        
        for index,p in enumerate(guess):
            if guess[index] != secret[index] and  dic_count.setdefault(p,0) > 0:               
                dic_count[p] -= 1
                cows += 1

        return "{0}A{1}B".format(bulls,cows)
    
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        secret_dict = collections.defaultdict(int)
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                secret_dict[s] += 1
        for i, g in enumerate(guess):
            if secret[i] != guess[i] and secret_dict[g]:
                cows += 1
                secret_dict[g] -= 1
        return str(bulls) + "A" + str(cows) + "B"



sol = Solution()

assert sol.getHint('1807','7810') == "1A3B"

assert sol.getHint('1123','0111') == "1A1B"