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

class Solution:

    def convert(self,  s,  numRows):
        cols=[]
        count,p =0,0 
        if numRows <=1 :
            return s
        
        while p < len(s):
            col = [''] * numRows
            if count % (numRows-1 ) ==0:  
                for i in range(numRows):
                    if p+i <len(s):
                        col[i] += s[p+i]  
                p += numRows
            else:
                col[numRows-count-1]=s[p]
                p += 1
            
            count = (count + 1)%(numRows-1)            
            cols.append(col)
        
        msg = ''
        for i in range(numRows):
            for j in range(len(cols)):
                if cols[j][i]!= "":
                    msg += cols[j][i]
            
        return msg


    def convert2(self,  s,  numRows):
        rows=[[] for i in range(numRows)] 
        count,p =0,0 
        if numRows <=1 :
            return s
        
        while p < len(s):            
            if count % (numRows-1 ) ==0: 
                for i in range(numRows):
                    if p+i <len(s):
                        rows[i] += s[p+i]               
                p += numRows
            else:                
                rows[numRows-count-1] += s[p]  
                p += 1
            
            count = (count + 1)%(numRows-1)          
           
        msg = ''
        for row in rows:
            msg +=''.join(row)
            
        return msg








sol = Solution()
#sol.convert('PAYPALISHIRING',3)
print (sol.convert('PAYPALISHIRING',4))