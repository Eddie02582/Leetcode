'''
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.
'''

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = 'qwertyuiopQWERTYUIOP'
        row_2 = 'asdfghjklASDFGHJKL'
        row_3 = 'zxcvbnmZXCVBNM'
        result = []
        for word in words:
            if all (s in  row_1 for s in word):
                result.append(word)
            elif all (s in  row_2 for s in word):
                result.append(word)
            elif all (s in  row_3 for s in word):
                result.append(word)
        return result
        
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = 'qwertyuiopQWERTYUIOP'
        row_2 = 'asdfghjklASDFGHJKL'
        row_3 = 'zxcvbnmZXCVBNM'
        result = []
        for word in words:            
            if all (s in  row_1 for s in set(word)):
                result.append(word)
            elif all (s in  row_2 for s in set(word)):
                result.append(word)
            elif all (s in  row_3 for s in set(word)):
                result.append(word)
        return result
        

    def findWords(self, words):
        row_1 = set('qwertyuiopQWERTYUIOP')
        row_2 = set('asdfghjklASDFGHJKL')
        row_3 = set('zxcvbnmZXCVBNM')
        result = []
        for word in words:            
            if row_1 | set(word) == row_1:
                result.append(word)
            elif row_2 | set(word) == row_2:
                result.append(word)
            elif row_3 | set(word) == row_3:
                result.append(word)
        return result    
        
    def findWords(self, words):
        ll = []
        a = set(['Q','W','E','R','T','Y','U','I','O','P'])
        b = set(['A','S','D','F','G','H','J','K','L'])
        c = set(['Z','X','C','V','B','N','M'])
        for i in words:
            ii = set(i.upper())
            if ii.intersection(a)==ii or ii.intersection(b)==ii or ii.intersection(c)==ii:
                ll.append(i)
        return ll        
        
        
        
        
        
        