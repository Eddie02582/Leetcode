# Longest Substring Without Repeating Characters


## 原題目:

```
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    
Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I
```

## 思路
使用一個布林値記錄目前向上還下,當頭或尾時,需轉向,這邊注意當s 長度為一需另外處理


## Code

#### Python

```
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1 :
            return s        
        row = [''] * numRows
        
        direDown = False
        currentRow = 0
        
        for i in range(len(s)):            
            row[currentRow] += s[i]
            
            if currentRow == 0 or  currentRow == numRows - 1:
                direDown = not direDown
                
            if direDown:
                currentRow += 1
            else:
                currentRow -= 1
        return ''.join(row)                    
```




