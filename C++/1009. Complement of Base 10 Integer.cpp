class Solution {
public:
    int bitwiseComplement(int n) {
        if (n==0)
            return 1;
        int temp = n;
        int t = 0;
        while (temp){
            temp = temp >> 1;
            t = (t << 1 )+ 1;
        }       
        return t^n;      
    }

    int bitwiseComplement_(int n) {
        if (n==0)
            return 1;
        int i = 0,res = 0;        
        while (n){
            res += ((n & 1)^1) << i;
            n >>= 1;
            i += 1;           
        }       
        return t^n;      
    }
};

int main(){
    Solution sol;
    sol.bitwiseComplement(5);



}