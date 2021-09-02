public class Solution {
    public int ArrayNesting(int[] nums) {
        int length = nums.Count();
        bool []visited = new bool[length];
        int res = 0;
        
        for(int i = 0;i<length;i++){
            if(!visited[i]){
                int j = i;
                int count = 0;
                
                while(!visited[j])
                {                    
                    count += 1;
                    visited[j] = true;
                    j = nums[j] ;
                }
                
                if(count >res)
                    res = count;
            }            
        }
        return res;
        
    }
}