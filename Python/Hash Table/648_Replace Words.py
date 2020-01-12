class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        import re
        sentence = " " +sentence
        for key in dict:
            sentence = re.sub("(?<=(\s))%s[a-z]+" %key,key, sentence)  
            #sentence = re.sub("%s[a-z]+" %key, key, sentence)
        print (sentence)
        return sentence [1:]
 

    def replaceWords__(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        import re
        array = sentence.split()       
        for key in dict:
            for i in range(len(array)):                
                array[i] = re.sub("^%s[a-z]+" %key, key, array[i])
        
        return " ".join(array)
        
sol = Solution()
assert sol.replaceWords(["a","b","c"],"aadsfasf absbs bbab cadsfafs") == "a a b c"
assert sol.replaceWords(["a", "aa", "aaa", "aaaa"],"a aa a aaaa aaa aaa aaa aaaaaa bbb baba ababa") == "a a a a a a a a bbb baba a"