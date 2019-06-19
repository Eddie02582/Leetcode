'''
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

'''
#!/usr/bin/python
# encoding=utf-8
class Solution:
    #my solutions
    #建立符合numRows長度的陣列來儲存row 值
    #如果count % ( numRows-1 ) ==0 表示第一欄 ,分別填入各字的行
    #如果不是填入numRows-count-1行值
    #最後在join
    def convert_row(self,  s,  numRows):
        if numRows <=1 :
            return s

        rows=['']*numRows
        count,p =0,0 

        while p < len(s):            
            if count % ( numRows-1 ) ==0: 
                for i in range(numRows):
                    if p + i < len(s):
                        rows[i] += s[p+i]               
                p += numRows
            else:                
                rows[numRows-count-1] += s[p]  
                p += 1
            
            count = (count + 1)%(numRows-1)     
            
        return ''.join(rows)     
    # leetcode sol         
    #上面類似的簡化
    #利用一個goingDown判斷向上還向下,如果到底或頭就反向

    def convert_sort_by_Row(self,  s,  numRows):     
        if numRows <= 1 :
            return s
            
        rows=['']*numRows 
        curRow = 0;
        goingDown = False
        
        for x in s :
            rows[curRow] += x
            if curRow == 0 or curRow == numRows-1:
                goingDown = not goingDown

            if goingDown:
                curRow += 1
            else:
                curRow -= 1          
         
        return ''.join(rows)     



        
    def convert_Visit_by_Row(self,  s,  numRows):       
        if numRows <=1 :
            return s
  
        ret = []
        n = len(s)
        cycleLen = 2 * numRows -2 
        
        for i in range(numRows):
            for j in range(0,n-i,cycleLen):
                ret.append(s[j+i])
                if i != 0 and i != numRows-1 and j + cycleLen -i < n:
                    ret.append(s[j + cycleLen -i])              
        return ''.join(ret)







sol = Solution()
#sol.convert('PAYPALISHIRING',3)
print (sol.convert_sort_by_Row('PAYPALISHIRING',4))