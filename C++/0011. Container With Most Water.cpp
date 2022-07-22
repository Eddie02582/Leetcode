class Solution {
public:
    int maxArea(vector<int>& height) {
        int start = 0;
        int end = height.size() - 1;
        int maxArea = 0,area = 0;        
        while (start < end)
        { 
            if(height[start] < height[end]){
                area = height[start] * (end - start);
                start++;
            }
            else{
                area = height[end] * (end - start);
                end--;
            }
            if(area > maxArea)
                maxArea = area;   
        }
        return maxArea;
    }
};