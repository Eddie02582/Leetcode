class Solution {
public:
    string addBinary(string a, string b) {
        string ans;
        int i = a.length()-1, j = b.length()-1;
        int carry = 0;
        
        while(i >= 0 || j >= 0 || carry){           
            carry +=   i < 0 ? 0 : (a[i--]-'0');
            carry +=   j < 0 ? 0 : (b[j--]-'0');   
            ans = (carry%2 ?"1":"0") + ans ;  
            carry/=2;
        }               
        return ans;
    }
};