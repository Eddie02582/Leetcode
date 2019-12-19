'''
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

'''

class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = {}
        for s in text:
            if s not in count:
                count[s] = 1
            else:
                count[s] += 1
        
        times = 0
        while True:
            for s in "balloon":
                if s not in count:
                    return times
                else:
                    count[s] -= 1
                if  count[s] < 0:
                    return times
            times += 1
        return times

    def maxNumberOfBalloons_min(self, text) 
        return min(text.count('b'),text.count('a'), text.count('l')//2, text.count('o')//2, text.count('n'))