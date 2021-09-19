# Permutation in String

## 原題目:
```
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:
	Input: s1 = "ab", s2 = "eidbaooo"
	Output: true
	Explanation: s2 contains one permutation of s1 ("ba").
	Example 2:

	Input: s1 = "ab", s2 = "eidboaoo"
	Output: false
```

這題的進階題找出s2裡符合s1 permutation的字元<br>
```
s1 = abbc,<br>
s2 = 'cbabadcbbabbcbabaabccbabc'
      ----  ---- ----      ---- 
              ----       ----  
                  ----			 
```				  
output:['cbab', 'cbba', 'abbc', 'bcba', 'cbab', 'cbab', 'babc']
	     
## 思路1
建立一個need 和window,need為符合字元的個數,window紀錄當下窗口的字元個數,當window == need 紀錄下來<br>
當遇到字元不在need,表示這窗口不符合,可以直接將l移到r+1,或是當window字元個數超過need,移動左邊指針直到window字元個數小於need

#### Python
```python
def find_permutation(s1,s2):
    window,need = {},{}
    for s in s1:
        need[s] = need.get(s,0) + 1
        
    ans = []
    l,r = 0,0
    while r < len(s2) :
        if s2[r] in need:
            window[s2[r]] =  window.get(s2[r],0) + 1
            if window == need:
                ans.append(s2[l:r + 1])   
                window[s2[l]] -= 1
                l += 1
            else:
                while window[s2[r]] > need[s2[r]]:                    
                    if s2[l] in window:
                        window[s2[l]] -= 1  
                    l += 1
            r += 1
        else:
            window = {}
            r += 1
            l = r      
    return ans
```
所以567這題可以簡化成

``` python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window,need = {},{}
        for s in s1:
            need[s] = need.get(s,0) + 1
       
        l,r = 0,0
        while r < len(s2) :
            if s2[r] in need:
                window[s2[r]] =  window.get(s2[r],0) + 1
                if window == need:
                    return True                
                while window[s2[r]] > need[s2[r]]:                    
                    if s2[l] in window:
                        window[s2[l]] -= 1  
                    l += 1
                r += 1
            else:
                window = {}
                r += 1
                l = r      
        return False
``` 

## 思路2
一樣的思路但使用r - l +1判斷長度是否符合,如果長度符合,那麼l指針必須向左移動,並移除l指針的元素
```
def find_permutation2(s1,s2):
	from collections import Counter,defaultdict
	need = Counter(s1)
	window = defaultdict(int)		   
	ans = []
	l,r = 0,0
	while r < len(s2) :
	
		if s2[r] in need:
			window[s2[r]] +=1
			
		if r - l + 1 ==len(s1):
			if window == need:
				ans.append(s2[l:r + 1])  
			if s2[l] in window:            
				window[s2[l]] -= 1
			l += 1        
		r += 1            
	return ans
```

所以567這題可以簡化成

``` python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        from collections import Counter,defaultdict
        need = Counter(s1)
        window = defaultdict(int)	
        l,r = 0,0
        while r < len(s2) :
        
        	if s2[r] in need:
        		window[s2[r]] +=1				
        		
        	if r - l + 1 ==len(s1):
        		if window == need:
        			return True
        		if s2[l] in window:            
        			window[s2[l]] -= 1
        		l += 1        
        	r += 1            
        return False  
``` 