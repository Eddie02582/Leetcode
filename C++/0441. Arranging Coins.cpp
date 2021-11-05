class Solution {
public:
    int arrangeCoins(int n) {
        long total = 0,count = 0;        
        while ( total < n){   
            count += 1;
            total += count;              
        }     
        return n != total ? count - 1:count; 
    }

    int arrangeCoins_bs(int n) {
        long left = 0,right = n;
       
        while(left <= right){
            long mid = left + (right - left)/2;
            long sum = mid * (mid + 1)/2;
            if(sum == n){
                return mid;
            }
            else if( n < sum){
                right = mid - 1;
            }
            else{
                left = mid + 1;
            }
        }
        return right;
    }
};