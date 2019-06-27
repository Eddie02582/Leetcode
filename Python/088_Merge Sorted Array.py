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

                
    def merge_simple(self, nums1, m, nums2, n): 
        i = m - 1
        j = n - 1
        count =  m + n 
        
        while count >= 0 :
            if i >=0 and j >=0:            
                if  nums2[j] >= nums1[i] :
                    nums1[i + j + 1] = nums2[j]
                    j -= 1
                else:  
                    nums1[i + j + 1] ,nums1[i]=  nums1[i],0         
                    i -= 1 
            elif i >= 0 :
                i -= 1 
                nums1[i + j + 1] ,nums1[i]=  nums1[i], 0              
            elif j >=0:
                nums1[i + j + 1] = nums2[j]
                j -= 1
            count -= 1        

    def merge(self, nums1, m, nums2, n):            
        i = m - 1
        j = n - 1
        while j >= 0 :
            if i < 0 or nums2[j] >= nums1[i]:
                nums1[i + j + 1]=nums2[j]
                j -= 1
            else:
                nums1[i + j + 1] = nums1[i]
                nums1[i] = 0
                i -= 1 



sol = Solution()
#assert sol.merge3( [1,2,3,0,0,0],3,[2,5,6],3) == [1,2,2,3,5,6] 
#assert sol.merge3( [1,2,2,4,5,0,0,0],5,[2,5,6],3) == [1,2,2,2,4,5,5,6] 
#assert sol.merge3( [2,0],1,[1],1) == [1,2] 