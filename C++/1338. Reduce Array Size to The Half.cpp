class Solution {
public:
    int minSetSize(vector<int>& arr) {
        int count = 0;
        int remove_count = 0;
        unordered_map<int,int> n_map ;
        for(auto n : arr){
            n_map[n]++;           
        }
        
        vector<int> numbers;
        for (auto x : n_map){
            numbers.push_back(x.second);
        }
        
        sort(numbers.begin(), numbers.end());
        
        for(int i = numbers.size()-1; i>=0; i--)
        {
            count += 1;
            remove_count += numbers[i];
            if(remove_count >= arr.size()/2)
                return count;
           
        } 
        return count;
        
        
    }
    int minSetSize_heapq(vector<int>& arr) {
        unordered_map<int,int>umap;     
        
        for(auto n : arr){
            umap[n]++;           
        }
        priority_queue<int> pq;        
        for(auto it: umap) 
            pq.push(it.second);
        
        int ans = 0, minus = 0;
        while(!pq.empty())
        {
            ans++;
            minus += pq.top();            
            if(minus >= (arr.size()/2)) 
               return ans;
            pq.pop();
        }
        return ans;        
    }
    int minSetSize(vector<int>& arr) {
        int cnt[100001] = {0};
        for (auto v : arr)
            cnt[v]++;

        int freq[100001] = {0};

        for (int v = 1; v < 100001; v++) 
            if (cnt[v]) freq[cnt[v]]++;

        int ans = 0;
        int left = (arr.size()+1)>>1;

        for (int f = 100000; left > 0; f--){
            while (freq[f] && left > 0) {
                left -= f;
                freq[f]--;
                ans++;
            }
        }

        return ans;       
    }
    
    
    
};