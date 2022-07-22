class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int reverse = 0;  
        int num = 0;
        while(num < 32){
            reverse = reverse<< 1;
            reverse += (n & 1);       
            n = n >> 1;           
            num++;
        }
        return reverse;
    }
};