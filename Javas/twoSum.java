class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer,Integer> record = new HashMap<Integer,Integer>();
        for ( int i = 0; i < nums.length; i++)
        {
            int num = target - nums[i];
            if(record.containsKey(num))
            {
                return new int[] {record.get(num),i};             
            }
            record.put( nums[i],i);
            
        }
        return new int[] {0,0};      
        
    }
}