# Two Sum


## 原題目:
```
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
```

## 思路1 
字母個數一樣,利用陣列或字典判斷個數是否一樣


#### Python

``` python
class Solution:   
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False    
        array = [ 0 for i in range(256)]
        for p,q in zip(s,t):
            array[ord(p)] += 1
            array[ord(q)] -= 1 
        
        return all( x==0 for x in array)
```  




也可以利用字典
``` python
class Solution: 
    def isAnagram_counter(self, s, t): 
        from collections import Counter          
        return Counter(s) == Counter(t)     
``` 

#### Java
``` java
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        int [] array = new int [256];
        for (int i = 0 ; i< s.length() ;i++){
            array[s.charAt(i)] += 1;
            array[t.charAt(i)] -= 1;
        }
        for (int i = 0 ;i <256 ;i++){
            if (array[i] != 0){
                return false;
            }
        }        
        return true;
    }
}
``` 





## 思路2
排序後相等 
``` python
class Solution:  
    def isAnagram_sorted(self, s, t):       
        return sorted(list(s)) == sorted(list(t))  
``` 








