# Minimum Cost For Tickets


## 原題目:
```
You have n  tiles, where each tile has one letter tiles[i] printed on it.

Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.

 

Example 1:

Input: tiles = "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
Example 2:

Input: tiles = "AAABBC"
Output: 188
Example 3:

Input: tiles = "V"
Output: 1


```

## 思路
本來以為是subsetII 和Permutations II的結合



#### Python
``` python
class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        visited = [False] * len(tiles)
        
        ans = []
        def backtracking(s):  
            if s:
                ans.append(s)                
            lastNumber = ""
            for i in range(0,len(tiles)):               
                if not visited[i] and tiles[i] != lastNumber :
                    lastNumber = tiles[i]
                    visited[i] = True
                    backtracking(s + tiles[i])
                    backtracking(s)
                    visited[i] = False
       
        backtracking("")      
        return len(set(ans))
``` 

## 思路 *****

讓我們先看下AAB能構成的結果：
```
A //剩餘A，B
AA AB //剩餘B，剩餘A
AAB ABA //不剩

B //剩餘A，A
BA //剩餘A
BAA //不剩
```
我們可以發現，先選擇一個字母開始，然後從剩餘的字母裡選擇1個，2個...直到用完所有字母，放到了第一個字母的後面。<br>

因此是一個遞歸的方法，先統計每個字母出現的多少次，然後從中選擇一個字母，再從剩下的字母中選擇，直到所有字母都用完為止。<br>

那為什麼使用統計字母出現的次數，而不是直接在原來的單詞上選擇呢？
<strong>這樣同樣的字母在相同的位置只會被選擇一次。例如AAB的第一個A和第二個A都可以組成AB，如果在單詞上選可能需要set進行去重，但是統計字母出現的次數的時候，在第一個位置選擇A的時候只會選擇一次。</strong>

``` python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        count = Counter(tiles)
        self.ans = 0
        
        def backtracking():          
            for key in count.keys():
                if count[key] >0:
                    count[key] -= 1
                    self.ans += 1
                    backtracking()                
                    count[key] += 1
        backtracking()
        return self.ans 

``` 

如果要列出所有組合
``` python
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import Counter
        
        count = Counter(tiles)
        ans = []
        
        def backtracking(s):          
            for key in count.keys():
                if count[key] >0:
                    count[key] -= 1
                    ans.append(s + key)
                    backtracking(s + key)                
                    count[key] += 1
        backtracking("")
        return len(ans)

``` 

