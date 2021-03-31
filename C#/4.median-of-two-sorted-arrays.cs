/*
 * @lc app=leetcode id=4 lang=csharp
 *
 * [4] Median of Two Sorted Arrays
 */

// @lc code=start
public class Solution {
    public double FindMedianSortedArrays(int[] nums1, int[] nums2) {
        int length = (nums1.Length + nums2.Length);
        int midl = (length + 1) / 2;
        int mid2 = (length + 1) / 2 + (length + 1) %　2 ;
        int index1 = 0,index2 = 0,count = 0;
        double median = 0 ,val = 0;

        
        while (count < mid2){            
            int val1 = index1 < nums1.Length ? nums1[index1]: int.MaxValue;
            int val2 = index2 < nums2.Length ? nums2[index2]: int.MaxValue;          
            if (val1 < val2){
                val = val1;
                index1 += 1;
            }
            else{
                val = val2;
                index2+= 1;     
            }    
            count += 1;
            if (count == midl)
                median += val;
            if (count == mid2)
                median += val;  
        }

        return (median)/ 2.0;

    }
}
// @lc code=end

