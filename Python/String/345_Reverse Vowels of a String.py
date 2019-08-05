#!/usr/bin/python
# encoding=utf-8
'''
345. Reverse Vowels of a String
Easy

385

700

Favorite

Share
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:

Input: "hello"
Output: "holle"
Example 2:

Input: "leetcode"
Output: "leotcede"
Note:
The vowels does not include the letter "y".
'''


class Solution:   

    def reverseVowels(self, s):
        vowels=[] 
        reverse=''        
        for x in s:
            if x in 'aeiouAEIOU':
                vowels.append(x)
                
        for y in s:
            if y not in 'aeiouAEIOU':
                reverse+=y
            else:
                reverse+=vowels.pop()     
        return reverse
        
    
    # ��ӫ��w���O�q�Y�ڧ�,�p�G���w��m���O�b�����N�[1,��P�ɳ��O�����N�洫�r��,���쥪����w�j�󵥩�k��
        
    
    def reverseVowels_pointer(self, s):
        vowels="aeiouAEIOU"
        l,r=0,len(s)-1
        letter = list(s)
        
        while l < r:
            if letter[l] not in vowels:
                l += 1
            if letter[r] not in vowels:
                r -= 1
            if letter[l] in vowels and letter[r] in vowels:
                letter[l],letter[r]=letter[r],letter[l]
                l,r=l+1,r-1                   
        return ''.join(letter)        
        
        
sol = Solution()

assert sol.reverseVowels("hello")=="holle"

assert sol.reverseVowels("leetcode")=="leotcede"

assert sol.reverseVowels_pointer("hello")=="holle"

assert sol.reverseVowels_pointer("leetcode")=="leotcede"









