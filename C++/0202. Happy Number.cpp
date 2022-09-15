class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> appear;  
        while(n != 1){           
            int new_n = 0;           
            while(n){               
                new_n +=   (n % 10) * (n % 10);                
                n = n /10;              
            }  
            n = new_n;
            if (appear.count(n))
                return false;
            appear.insert(n);
        }
        return true;       
    }
};