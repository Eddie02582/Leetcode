'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

'''


class Solution(object):
    def maxArea_brute_force(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        length = len(height)
        for i in range(length):
            for j in range(i + 1,length):
                h = min(height[i],height[j])
                area = (j - i) * h 
                max_area = max(max_area,area)
        return max_area
        
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """            
        max_area = 0
        length = len(height)
        l,r = 0 ,length - 1 
        
        while l < r :
            h = min(height[l],height[r])
            area = (r - l) * h
            max_area = max(max_area,area)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1  
            
        return max_area
        

        
        
        
        
        
        
        
        
        
        