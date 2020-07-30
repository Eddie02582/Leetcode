class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        result = [-1,-1]        
        l ,r = 0 ,len(nums) - 1       
        while l < r:
            mid = l + (r - l)//2
            if target <= nums[mid]:
                r = mid
            else :
                l = mid + 1
        if nums[l] == target:
            result[0] = l

        l ,r = 0 ,len(nums) - 1  
        while l < r:
            mid = l + (r - l + 1)//2
            if target >= nums[mid]:
                l = mid
            else :
                r = mid - 1
        if nums[l] == target:
            result[1] = l  
       
        return result
    def searchRange(self, nums, target):
        start = 0; end = len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if nums[start] == nums[end] == target:
                return [start, end]
            if nums[mid] < target:
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                if nums[start] != target: start += 1
                if nums[end] != target: end -= 1
        return [-1,-1]
            

    
