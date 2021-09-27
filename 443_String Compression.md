# String Compression


## 原題目:
```
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
Example 4:

Input: chars = ["a","a","a","b","b","a","a"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","3","b","2","a","2"].
Explanation: The groups are "aaa", "bb", and "aa". This compresses to "a3b2a2". Note that each group is independent even if two groups have the same character.
 

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.
```

## 思路

簡單版的壓縮字串
字符串aabcccccaaa 會變成a2b1c5a3。若壓縮後的字符串沒有變短，則返回原先的字符串。
這邊注意最後一筆要額外加

```
def string_compression(s):
    if not s:
        return ""
    ans = ""  
    count = 0   
    for i in range(0,len(s)):
        if i != 0 and s[i] != s[i - 1]:
            ans += f'{s[i-1]}{count}'
            count = 0        
        count += 1        
    ans += f'{s[-1]}{count}'      
    return  min(s,ans,key = len)
```

壓縮字串的變形,題目給char陣列,inplace修改陣列,這邊注意count 為1不需要壓縮


#### Python

``` python
class Solution:
    
    def update_arry(self,arr,loc,c,count):
        arr[loc] = c   
        if count > 1:
            for s in str(count):
                loc += 1
                arr[loc] = s            
        return loc +1            
    
    def compress(self, chars: List[str]) -> int:
        if len(chars) <2 :
            return len(chars)
        
        count,loc = 0,0  
        for i in range(len(chars)):            
            if i != 0 and chars[i] != chars[i- 1]:  
                loc =self.update_arry(chars,loc,chars[i- 1],count)                       
                count = 0
            count += 1        
        loc = self.update_arry(chars,loc,chars[-1],count)   
       
        return loc
    
       
``` 








