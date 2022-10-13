class Solution {
public:
    bool checkInclusion_(string s1, string s2) {        
        int freqS1 [26] = {0};
        int freqS2 [26] = {0}; 
        
        int char_cnt = 0;
        int match = 0;

        for(auto c :s1){
            if(!freqS1[c - 'a'])
                char_cnt++;
            freqS1[c - 'a']++;                
        }
        
        int left = 0,right = 0;   
        while (right < s2.size()){  
            freqS2[s2[right] -'a']++;  
            if(freqS2[s2[right] -'a']  == freqS1[s2[right] -'a']){
                match++;
            }
            else{                
                while(freqS2[s2[right] -'a'] > freqS1[s2[right] -'a']){                
                    if(freqS1[s2[left] -'a'] > 0 && freqS2[s2[left] -'a']  == freqS1[s2[left] -'a']){
                            match--;
                    }
                    freqS2[s2[left] -'a']--;
                    left++;
                }  
            }
            
            if(match == char_cnt)
                 return true;   
            right++;            
        }
        return false;
    }
    
    bool checkArrayEqual(int a[], int b[]){
        for(int i=0; i<26; i++){            
             if(a[i]!=b[i]) 
                return false;
        }
        return true;
    }


    bool checkInclusion(string s1, string s2) {        
        int freqS1 [26] = {0};        
        
        for(auto c :s1){         
            freqS1[c - 'a']++;         
        }
        
        int left = 0,right = 0;   
        while (right < s2.size()){              
            freqS2[s2[right] -'a']++;
            
            if (right - left + 1 == s1.size()){
                //check 
                if(checkArrayEqual(freqS1,freqS2))
                    return true;                
                
                freqS2[s2[left] -'a']--;
                left++;
                
            }
            right++;  
        }
        return false;
    }
};
    
    
    
    
    
    
    
    
    
    



