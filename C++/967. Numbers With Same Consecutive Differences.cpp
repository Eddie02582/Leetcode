class Solution {
public:
    vector<int> numsSameConsecDiff(int n, int k) {
        //bfs
        vector<int> ans;        
        for(int i = 1;i <= 9;i++){            
            if((i + k) <= 9 || (i -k) >= 0)
            {             
                int count = 1;
                queue<int> q;
                q.push(i);                
                while(count < n  && !q.empty()){ 
					count++;   					
                    int size = q.size();                    
                    for(int j = 0; j < size;j++){
                       int val = q.front();                       
                       q.pop();
                       int res =  val%10;                         
					   if( count == n){
                           if (k == 0)
                               ans.push_back(val*10 + res); 
                           else{
                               if((res + k) <=9)
                                  ans.push_back(val*10 + (res + k));                        
                               if((res - k) >=0)
                                  ans.push_back(val*10 + (res - k)); 
                           }
					   }
					   else{
                            if (k == 0)
                               q.push(val*10 + res); 
                           else{
							if((res + k) <=9)
							  q.push(val*10 + (res + k));                        
							if((res - k) >=0)
							  q.push(val*10 + (res - k));		
                           }
					   }
                    }                          
                }              
                
            }  
        }
      
        return ans;
        
    }
	
    vector<int> numsSameConsecDiff_dfs(int n, int k) {        
        vector<int> ans;    
		for(int i = 1;i <= 9;i++){  
			if((i + k) <= 9 || (i -k) >= 0){
				dfs(n - 1,k,i,ans);
			}
		}	
        return ans;
        
    }
	
	void dfs(int n,int k,int val,vector<int> &ans) {
		if (n == 0)
			ans.push_back(val);
		else{
			int res = val % 10;
			if(k == 0){				
				dfs(n - 1,k,val *10 +res,ans);
			}
			else{
				if(res + k <= 9)
					dfs(n - 1,k,val *10 + res + k,ans);
				if(res - k >=0)
					dfs(n - 1,k,val *10 +res - k,ans);
			}         
		}
		return;
	}
	
};