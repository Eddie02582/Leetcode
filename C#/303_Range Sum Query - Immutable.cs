using System.Collections.Generic;
public class NumArray {
    
    List <int> sum = new List<int>();
    int [] nums;
    public NumArray(int[] nums) {
        this.nums = nums;
        sum.Add(0);
        for (int i = 0;i<nums.Count();i++)
        {            
           sum.Add(nums[i] + sum[i]);            
        }
        
    }
    
    public int SumRange(int i, int j) {
        return sum[j+1] - sum[i];
    }
}