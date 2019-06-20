'''
Given a non negative integer number num. For every numbers i in the range 0 ? i ? num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]
Example 2:

Input: 5
Output: [0,1,1,2,1,2]
Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

Next challenges:
    Number of 1 Bits


'''

'''
7 / 2 =3 ..1

3 /2  =1...1

1 /2  =0 ...1

5 /2 =2...1

2 /2 =1...0

1 /2=0...1

4 /2 =2...0

2 /2 =1...0

1/2 =0 ...1 




'''




class Solution(object):
    def countBits_format(self, num):
        return [ format(i,'b').count('1') for i in range(0,num+1)]
        
        
    def countBits_res(self, num):
        result=[]
        for i in range(0,num+1):
            count=0
            while i :
                i,res=divmod(i, 2)        
                if res==1:
                    count+=1
            result.append(count)
        return result       
        
    def countBits_res(self, num):
        result=[]
        for i in range(0,num+1):
            count=0
            for i in range (0,32):
                if n >> i & 1 == 1:
                    count+=1
            result.append(count)
        return result           
        
        
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        list_ = [0 for x in range(num+1)]
        for i in range(1, num+1):
            k = i
            k = k & 1
            if k == 0: #even 3:0011 6:0110
                list_[i] = list_[i >> 1]
            else: #old
                list_[i] = 1 + list_[i-1]
        return list_        
        
        
def bin(num):
    for i in range(num):
        print (format(i,'b'))
        
        
sol=Solution()
assert sol.countBits(2)==[0,1,1]

assert sol.countBits(5)==[0,1,1,2,1,2]







