class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dict ={
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'], 
            '9':['w','x','y','z'],  
        }       
                
        def helper(array,digits):        
            if digits:
                number,digits = digits[0],digits[1:]                
                result = []  
                if not array:#for first
                    return helper(dict[number],digits)                
                for s in array:
                    for letter in dict[number]:
                        result.append(s + letter)                
                return helper(result,digits)    
            return array            
     
        return helper([],digits)