# Merge Sorted Array


## 原題目:
```
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

## 思路

1. 一般來說把nums2 放入nums1 排序即可
2. 利用雙指針比較nums1 和 nums2 的值小的先填當值填完即結束



## Code

#### Python
nums2 放入nums1 排序即可,底下用汽泡排序法排

``` python
class Solution(object):
    def merge_bubble_sort(self, nums1, m, nums2, n):        
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i] 
        
        for i in range(len(nums1)):
            bsweep=False
            for j in range(0,len(nums1) - i - 1):
                if nums1[j] >nums1[j+1]:
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
                    bsweep = True
            if not bsweep:
                break
```  



我們需要三个指針：</br>

&nbsp&nbsp1.current 記錄目前前填到的位置</br>

&nbsp&nbsp2.i 記錄 nums1 數組處理到哪個元素</br>

&nbsp&nbsp3.j 記錄 nums2 數組處理到哪個元素</br>


分三種情況：</br>

&nbsp&nbsp 1.當i,j >=0 時 num2[j]>=num1[i] 填值,反過來時要小心,當num1[i]填入nums1[current]時,原本num1[i]須改成0,或是nums2[j]</br>

&nbsp&nbsp 2.j >=0,i < 0,直接填值

&nbsp&nbsp 3.i >=0,j < 0,離開,因為nums本身已經排序,後面不需要排



&nbsp&nbsp1.當i,j >=0 時 num2[j]>=num1[i] 填值,反過來時要小心,當num1[i]填入nums1[current]時,原本num1[i]須改成0,或是nums2[j] </br>
&nbsp&nbsp2.當只剩 i >= 0,num1[i]填入nums1[current]時,原本num1[i]須改成0 </br>
&nbsp&nbsp3.當只剩 j >= 0,num2[j]直接填入nums1[current] </br>

note: 為何num2[j]>=num1[i] 可以直接填值,因為當要填入num1[i + j + 1]時,值都是0(num1[i] >num2[j] 換掉或是一開始陣列長度(m)外的0 )


``` python
class Solution(object):
    def merge(self, nums1, m, nums2, n): 
        i = m - 1
        j = n - 1
        
        current = m + n - 1
        while current >= 0 :
            if i >=0 and j >=0:            
                if  nums2[j] >= nums1[i] :
                    nums1[current] = nums2[j]
                    j -= 1
                else:  
                    nums1[current] ,nums1[i]=  nums1[i],0       
                    i -= 1 
            elif j >=0 :   
                nums1[current] = nums2[j]
                j -= 1       
            else :
                break
            current -= 1
        return nums1
      
``` 

由上面可知當j < 0時表示不需要再插入,所以分兩種情況<br>

&nbsp&nbsp1.當i,<0 或 num2[j]>=num1[i] 填值</br>
&nbsp&nbsp2.num2[j]<num1[i] 且 i,j >= 0



``` python
class Solution(object):
    def merge(self, nums1, m, nums2, n): 
        i = m - 1
        j = n - 1           
        current = m + n - 1
        while j >= 0 :                  
            if  i < 0 or nums2[j] >= nums1[i] :
                nums1[current] = nums2[j]
                j -= 1
            else:  
                nums1[current] ,nums1[i]=  nums1[i], 0 
                #nums1[current] ,nums1[i]=  nums1[i],nums2[j]
                i -= 1   
            current -= 1
``` 



















