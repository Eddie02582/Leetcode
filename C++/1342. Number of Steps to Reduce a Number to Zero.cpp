class Solution {
public:
    int numberOfSteps(int num) {
        int step = 0;
        
        while(num){             
            if((num & 1) == 0){
                num = num >>1;
            }
            else{
                num -= 1;
            }
            step += 1;
        }
        return step;
    }
};