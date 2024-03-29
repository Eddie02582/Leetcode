class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        mapping = {'2':"abc",'3':"def",'4':'ghi','5':'jkl','6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}
        ans = []
        def backtracking(word,start):
            if len(word) == len(digits):
                ans.append(word)
                return
            for i in range(start,len(digits)):
                for letter in mapping[digits[i]]:
                    backtracking(word + letter,i + 1)        
        backtracking("",0)   
        return ans
        
        
    def letterCombinations_backtrack(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
                
        def backtrack(combination, next_digits):
            # if there is no more digits to check
            if len(next_digits) == 0:
                # the combination is done
                output.append(combination)
            # if there are still digits to check
            else:
                # iterate over all letters which map 
                # the next available digit
                for letter in phone[next_digits[0]]:
                    # append the current letter to the combination
                    # and proceed to the next digits
                    backtrack(combination + letter, next_digits[1:])
                    
        output = []
        if digits:
            backtrack("", digits)
        return output
        
    def letterCombinations_bfs(self, digits: str) -> List[str]:
        lookup = {"2":"abc","3":"def","4":"ghi",                  
                  "5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
                 }        
        from collections import deque    
        
        ans = deque([""])          
        for digit in digits:           
            for _ in range(len(ans)):  
                s = ans.popleft()
                for letter in lookup[digit]:
                    ans.append(s + letter)                      
        return ans if digits else []