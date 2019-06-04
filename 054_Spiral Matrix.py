'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''
#!/usr/bin/python
class Solution:
    ## 順序是[E,S,W,N],只要碰壁 或是 數字在Output 陣列裡面,回到上一步 改方向,直到所有值取出

    def spiralOrder_simple(self, matrix):   
        if matrix == []:
            return []
        row,col,count=0,0,0
        len_row ,len_col =len(matrix) ,len(matrix[0])    
        output=[]
        col_step=[1,0,-1,0]
        row_step=[0,1,0,-1]      
        
        while len(output) < len_row*len_col:

            if  0 <= row < len_row and  0 <= col < len_col and matrix[row][col] not in output:            
                output.append( matrix[row][col])
            else:
                row -= row_step[count]
                col -= col_step[count] 
                count = ( count + 1 )  % 4

            row += row_step[count]
            col += col_step[count]  
                
        return output

    # 使用遞迴 ,寫個一函數 ,取出分別上右下左,最後將剩下的陣列在一次傳入,注意一為陣列的情況   
    def spiralOrder(self, matrix):   
        if matrix == []:
            return []
        else:
            output=self.side(matrix,[])            
            return output                
        
        
    def side(self, matrix,output=[]):
        m = len(matrix)
        n = len(matrix[0]) if m>0 else 0

        if m <= 0 or n <= 0:
            pass
        elif m == 1:
            output += matrix[0]            
        elif n == 1:
            output += [matrix[r][0] for r in range(m)]   
        else:
            m ,n =len(matrix) ,len(matrix[0])    
            #add top 
            output += matrix[0]
            #add right   matrix[1][-1] ....
            output += [ arr[-1] for arr in matrix[1:] ]
            
            #add right   matrix[1][-1] ....
            #output += [matrix[-1][f] for f in range(n-2,-1,-1)]
            output += [ matrix[-1][col] for col in range(-2,-n-1,-1) ]
            
            # ## add left col (except top-bot left corners)
            #[matrix[r][0] for r in range(m-2, 0, -1)]
            output += [ matrix[row][0] for row in range(-2,-m,-1) ]
            
            matrix = [list(arr[1:-1]) for arr in matrix[1:-1]]

            self.side(matrix,output)      
        return output                
        
        
        
sp =Solution()
assert sp.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])==[1,2,3,6,9,8,7,4,5]

assert sp.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])==[1,2,3,4,8,12,11,10,9,5,6,7]

assert sp.spiralOrder([[1]])==[1]
assert sp.spiralOrder([[]])==[]

