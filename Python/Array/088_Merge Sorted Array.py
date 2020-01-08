class Solution(object):
    def merge_bubble_sort(self, nums1, m, nums2, n):        
        for i in range(len(nums2)):
            nums1[m + i] = nums2[i] 
        
        for i in range(len(nums1)):
            bsweep = False
            for j in range(0,len(nums1) - i - 1):
                if nums1[j] >nums1[j+1]:
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
                    bsweep = True
            if not bsweep:
                break

                
    def merge(self, nums1, m, nums2, n): 
        while n or m :
            if  not m or  (n  and nums2[n - 1] > nums1[m - 1]):
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1            
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
   
        return  nums1   



    def merge_simple(self, nums1, m, nums2, n): 
        while n:
            if  not m  or  nums2[n - 1] > nums1[m - 1]:
                nums1[n + m - 1] = nums2[n - 1]
                n -= 1            
            else:
                nums1[n + m - 1] = nums1[m - 1]
                m -= 1
   
        return  nums1 








sol = Solution()
assert sol.merge( [1,2,3,0,0,0],3,[2,5,6],3) == [1,2,2,3,5,6] 
assert sol.merge( [1,2,2,4,5,0,0,0],5,[2,5,6],3) == [1,2,2,2,4,5,5,6] 
assert sol.merge( [2,0],1,[1],1) == [1,2] 